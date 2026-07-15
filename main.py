import os
from random import randint
from pathlib import Path

from agent_framework import Agent, SkillsProvider, tool
from agent_framework.foundry import FoundryChatClient
from agent_framework_foundry_hosting import ResponsesHostServer
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
from pydantic import Field
from typing_extensions import Annotated

load_dotenv(override=True)

SEATTLE_WEATHER = {
    "downtown": ["drizzle", "cloudy", "light rain", "sun breaks"],
    "capitol hill": ["cloudy", "sun breaks", "light rain"],
    "fremont": ["drizzle", "overcast", "sun breaks"],
}

SEATTLE_NEIGHBORHOOD_TIPS = {
    "downtown": "Walkable core, great for first-time visits and transit access.",
    "capitol hill": "Best nightlife and coffee density. Great if you want to explore on foot.",
    "fremont": "Quirky neighborhood with breweries and easy access to the canal trail.",
}

def _read_required_env() -> tuple[str, str]:
    project_endpoint = os.getenv("FOUNDRY_PROJECT_ENDPOINT") or os.getenv(
        "PROJECT_ENDPOINT"
    )
    model_name = os.getenv("AZURE_AI_MODEL_DEPLOYMENT_NAME") or os.getenv(
        "MODEL_DEPLOYMENT_NAME"
    )

    if not project_endpoint:
        raise RuntimeError(
            "Missing project endpoint. Set FOUNDRY_PROJECT_ENDPOINT (preferred) "
            "or PROJECT_ENDPOINT."
        )
    if not model_name:
        raise RuntimeError(
            "Missing model deployment name. Set AZURE_AI_MODEL_DEPLOYMENT_NAME "
            "(preferred) or MODEL_DEPLOYMENT_NAME."
        )
    return project_endpoint, model_name


def _create_skills_provider() -> SkillsProvider:
    skills_root = Path(
        os.getenv("SEATTLE_SKILLS_ROOT", str(Path(__file__).parent / "skills"))
    )
    return SkillsProvider.from_paths(
        skill_paths=skills_root,
        disable_load_skill_approval=True,
        disable_read_skill_resource_approval=True,
    )


@tool(approval_mode="never_require")
def get_seattle_weather(
    neighborhood: Annotated[
        str, Field(description="Seattle neighborhood name, such as Downtown.")
    ],
) -> str:
    """Get a simple weather summary for a Seattle neighborhood."""
    key = neighborhood.strip().lower()
    conditions = SEATTLE_WEATHER.get(key, ["cloudy", "light rain", "sun breaks"])
    return f"{neighborhood}: {conditions[randint(0, len(conditions) - 1)]}, high near {randint(58, 74)}F."


@tool(approval_mode="never_require")
def get_neighborhood_tip(
    neighborhood: Annotated[
        str, Field(description="Seattle neighborhood name, such as Fremont.")
    ],
) -> str:
    """Get a practical travel tip for a Seattle neighborhood."""
    key = neighborhood.strip().lower()
    return SEATTLE_NEIGHBORHOOD_TIPS.get(
        key,
        "Great option for exploring Seattle. Check transit times and nearby cafes.",
    )


def main() -> None:
    project_endpoint, model_name = _read_required_env()
    skills_provider = _create_skills_provider()

    client = FoundryChatClient(
        project_endpoint=project_endpoint,
        model=model_name,
        credential=DefaultAzureCredential(),
    )

    agent = Agent(
        client=client,
        instructions=(
            "You are a concise Seattle trip assistant. "
            "Use get_seattle_weather for weather questions and "
            "get_neighborhood_tip for neighborhood guidance."
        ),
        tools=[get_seattle_weather, get_neighborhood_tip],
        context_providers=[skills_provider],
        default_options={"store": False},
    )

    server = ResponsesHostServer(agent)
    server.run()


if __name__ == "__main__":
    main()
