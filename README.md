# Foundry Hosted Agent Learning Sample (Current Stack)

This repository is updated to the current hosted-agent pattern for Microsoft Foundry:

- **Agent Framework + Foundry hosting packages**
- **Responses protocol (`/responses`)**
- **`azd` deployment flow with `azure.yaml`**
- **Two local tools** in `main.py`:
  - `get_seattle_weather`
  - `get_neighborhood_tip`
- A file-based **Agent Skill** in `skills/seattle-activities/SKILL.md` loaded dynamically via `SkillsProvider`.

## What changed vs older samples

1. Old `azure-ai-agentserver-agentframework` usage was replaced with:
   - `agent-framework-foundry`
   - `agent-framework-foundry-hosting`
2. Agent setup now uses:
   - `FoundryChatClient`
   - `ResponsesHostServer`
   - `SkillsProvider.from_paths(...)` for dynamic skill loading
3. Env vars now follow current Foundry naming:
   - `FOUNDRY_PROJECT_ENDPOINT`
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME`
4. Added `azure.yaml` so you can run:
   - local: `azd ai agent run`
   - remote deploy: `azd provision` + `azd deploy`

## Prerequisites

- Python **3.13+**
- [Azure Developer CLI (`azd`) 1.25.3+](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)
- Foundry extension for azd:

  ```bash
  azd ext install microsoft.foundry
  ```

- A Foundry project with a model deployment (for example `gpt-5.4-mini`)

## Authentication (when you need it)

You need Azure auth in two places:

1. **Before local Python run (`python main.py`)**  
   This sample prefers `azd` identity first, then `az`, then managed identity:

   ```bash
   azd auth login
   az login
   ```

2. **Before azd commands (`provision`, `deploy`, `invoke`, `monitor`)**  
   Authenticate azd:

   ```bash
   azd auth login
   ```

If you see 403 errors with `AIServices/agents/write`, your local credential likely resolved to the wrong tenant/account. Re-run `azd auth login` in the correct tenant and retry.

## Setup virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configure environment variables

Use `.env.example` as a template:

```bash
cp .env.example .env
```

Set:

- `FOUNDRY_PROJECT_ENDPOINT`
- `AZURE_AI_MODEL_DEPLOYMENT_NAME`
- Optional: `SEATTLE_SKILLS_ROOT` (defaults to `./skills`)

## Dynamic skill loading (Agent Framework built-in)

This sample uses Agent Framework's built-in **progressive disclosure** skill flow:

1. The skill is advertised by name/description.
2. The agent loads full skill instructions on demand (`load_skill`).
3. The agent reads skill resources only as needed (`read_skill_resource`).

Implementation is in `main.py`:

```python
skills_provider = SkillsProvider.from_paths(skill_paths=Path(__file__).parent / "skills")
agent = Agent(..., context_providers=[skills_provider])
```

This keeps base prompt context small and lets the harness load skill detail only for relevant tasks.

## Run locally

```bash
source .venv/bin/activate
python main.py
```

In another terminal:

```bash
curl -sS -H "Content-Type: application/json" -X POST http://localhost:8088/responses \
  -d '{"input":"What is the weather in Capitol Hill and give me one neighborhood tip?","stream":false}'
```

Try the skill-focused prompt:

```bash
curl -sS -H "Content-Type: application/json" -X POST http://localhost:8088/responses \
  -d '{"input":"Give me Seattle activities for Capitol Hill this evening.","stream":false}'
```

## Deploy to Foundry with azd

From this folder:

```bash
azd provision
azd deploy
```

Invoke the deployed agent:

```bash
azd ai agent invoke "What is the weather in Fremont and where should I stay nearby?"
```

## See traces and logs

1. **Foundry portal traces**: open your project in [https://ai.azure.com](https://ai.azure.com), go to the hosted agent and open its trace/log views.
2. **CLI live logs**:

   ```bash
   azd ai agent monitor --follow
   ```

Foundry hosted agents inject telemetry configuration (Application Insights / OpenTelemetry) at runtime, so traces and logs are available after invocation.

## References

- [Quickstart: Deploy your first hosted agent](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=azd)
- [Deploy a hosted agent](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent)
- [Invoke a hosted agent](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/invoke-hosted-agent)
- [Monitor hosted agent logs](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/monitor-hosted-agent-logs)
