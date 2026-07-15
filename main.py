import os
from random import randint
from pathlib import Path

from agent_framework import Agent, tool
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

SEATTLE_ACTIVITIES = {
    "downtown": [
        "Pike Place Market food walk",
        "Seattle Art Museum",
        "Waterfront ferris wheel at sunset",
    ],
    "capitol hill": [
        "Volunteer Park Conservatory",
        "Indie coffee crawl on Pike/Pine",
        "Live music at neighborhood venues",
    ],
    "fremont": [
        "Fremont Sunday Market",
        "Canal trail bike ride",
        "Brewery tasting flight",
    ],
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


def _load_skill_instructions() -> str:
    default_skill_path = Path("skills/seattle-activities.md")
    configured_path = Path(
        os.getenv("SEATTLE_ACTIVITY_SKILL_PATH", str(default_skill_path))
    )
    if not configured_path.exists():
        return (
            "Skill unavailable: seattle-activities. "
            "Still provide helpful Seattle travel suggestions."
        )
    return configured_path.read_text(encoding="utf-8").strip()


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


@tool(approval_mode="never_require")
def get_local_activities(
    neighborhood: Annotated[
        str, Field(description="Seattle neighborhood name, such as Capitol Hill.")
    ],
    interest: Annotated[
        str, Field(description="Interest such as food, outdoors, museums, or nightlife.")
    ] = "general",
) -> str:
    """Get local Seattle activity ideas for a neighborhood and interest."""
    key = neighborhood.strip().lower()
    ideas = SEATTLE_ACTIVITIES.get(
        key,
        [
            "Coffee shop and bookstore pairing",
            "Neighborhood park walk",
            "Local food hall visit",
        ],
    )
    return (
        f"{neighborhood} activity ideas ({interest}): "
        + "; ".join(f"- {item}" for item in ideas)
    )


def main() -> None:
    project_endpoint, model_name = _read_required_env()
    skill_instructions = _load_skill_instructions()

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
            "get_neighborhood_tip for neighborhood guidance. "
            "Use get_local_activities for activity planning.\n\n"
            "Skill: seattle-activities\n"
            f"{skill_instructions}"
        ),
        tools=[get_seattle_weather, get_neighborhood_tip, get_local_activities],
        default_options={"store": False},
    )

    server = ResponsesHostServer(agent)
    server.run()


if __name__ == "__main__":
    main()
