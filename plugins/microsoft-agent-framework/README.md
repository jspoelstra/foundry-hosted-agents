# microsoft-agent-framework

Curated APM plugin containing the official **Microsoft Agent Framework** (MAF) Python SDK skill for building persistent agents on Azure AI Foundry.

This skill comes from the official Microsoft repository:
**https://github.com/microsoft/skills** (specifically the `azure-sdk-python` plugin).

## Included Skill

This plugin includes a focused selection:

- **agent-framework-azure-ai-py** — Build persistent agents using the Microsoft Agent Framework Python SDK (`agent-framework-azure-ai`). Covers `AzureAIAgentsProvider`, hosted tools (Code Interpreter, File Search, Web Search), MCP integration, `AgentThread` for conversation persistence, streaming responses, structured outputs with Pydantic, function tools, and multi-tool agents.

## Why Curated?

The full `azure-sdk-python` plugin from Microsoft contains 39+ skills. This wrapper extracts only the high-value Microsoft Agent Framework skill so you can use the official patterns without pulling in unrelated Azure SDK guidance (Cosmos DB, Event Hubs, App Configuration, etc.).

This keeps context lean while giving you first-class support for the recommended way to build stateful, tool-using agents on Foundry.

## Installation (within devpack or dependent projects)

```bash
apm install ./plugins/microsoft-agent-framework --target agent-skills
```

After installation, the skill will be available in `.agents/skills/agent-framework-azure-ai-py` and can be invoked via `/skills agent-framework-azure-ai-py` or by direct reference.

## Usage Tips

- Use this when you want to build **persistent, stateful agents** in Python that live on Azure AI Foundry.
- The skill is async-first — always use `async with` and `async def`.
- Prefer `DefaultAzureCredential` + context managers (the skill emphasizes this strongly).
- Combine with the `microsoft-foundry` / `foundry-hosted-agents` skills from the sibling `microsoft-foundry-agents` plugin for the full deployment + observability story.

## Attribution

All skill content is sourced from Microsoft and remains under the original license (MIT).

Original source: https://github.com/microsoft/skills (azure-sdk-python / agent-framework-azure-ai-py)

## Related Plugins in This Pack

- `microsoft-foundry-agents` — For the broader Foundry platform (hosted agent deployment, evaluation, observability, models).
- `azure-infrastructure-architecture` — For surrounding Azure infrastructure (Bicep, AKS, Well-Architected).

## Future Improvements

- Add the .NET / TypeScript / Java MAF equivalents when they stabilize in the upstream catalog.
- Consider adding a lightweight "MAF architect" agent persona.

Contributions and requests for additional Microsoft Agent Framework coverage are welcome.