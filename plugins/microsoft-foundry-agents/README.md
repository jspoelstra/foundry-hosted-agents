# microsoft-foundry-agents

Curated APM plugin containing high-value **Microsoft AI Foundry** (Azure AI Foundry) agent skills.

These skills come from the official Microsoft repository:
**https://github.com/microsoft/skills** (specifically the `azure-skills` plugin).

## Included Skills

This plugin includes a focused, high-signal selection:

- **microsoft-foundry** — The main router skill. Maps user intent to the correct sub-skill and discovery surface (Foundry MCP, azd, docs, etc.). Excellent entry point for anything Foundry-related.
- **foundry-hosted-agents** — Building, deploying, and managing containerized hosted agents (Responses / Invocations protocols).
- **foundry-observability** — Tracing, evaluation (batch + continuous), prompt optimization, and production monitoring.
- **foundry-models** — Model discovery, preset/custom deployments, capacity planning, and quota management.

## Why Curated?

The full Microsoft Foundry skill set is very comprehensive (and quite large). This plugin selects the most frequently useful skills for day-to-day agent development work, while keeping context manageable.

## Installation (within devpack or dependent projects)

```bash
apm install ./plugins/microsoft-foundry-agents --target agent-skills
```

After installation, the skills will be available in `.agents/skills/` and can be invoked via `/skills microsoft-foundry`, etc.

## Usage Tips

- Start with the `microsoft-foundry` skill for most tasks — it acts as an intelligent router.
- For deep evaluation/optimization work, bring in `foundry-observability`.
- For anything related to deploying custom code as agents, use `foundry-hosted-agents`.

## Attribution

All skill content is sourced from Microsoft and remains under the original license (MIT).

Original source: https://github.com/microsoft/skills

## Future Improvements

- Add more sub-skills on demand (finetuning, memory, toolboxes, governance, etc.)
- Create a lightweight wrapper skill tailored for non-Azure-MCP environments (Grok, pure Copilot, etc.)

Contributions and requests for additional Foundry skills are welcome.