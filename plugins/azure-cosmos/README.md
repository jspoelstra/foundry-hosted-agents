# azure-cosmos

Curated APM plugin containing high-value **Azure Cosmos DB** production patterns for Python (with FastAPI).

This skill comes from the official Microsoft repository:
**https://github.com/microsoft/skills** (specifically the `azure-sdk-python` plugin).

## Included Skill

- **azure-cosmos-db-py** — Production-grade Cosmos DB NoSQL service implementation. Covers:
  - Dual authentication (DefaultAzureCredential in Azure + emulator key for local dev)
  - Singleton client module with proper lifecycle management
  - Five-tier Pydantic model pattern (Base / Create / Update / Response / InDB)
  - Clean service layer with CRUD, validation, and graceful degradation
  - Partition key strategies and cross-partition query guidance
  - Parameterized queries and security best practices
  - Full TDD patterns with pytest fixtures for mocking
  - Ready-to-use templates in `assets/`

## Why Curated?

The `azure-sdk-python` bundle contains many SDK skills. This wrapper extracts the single highest-signal Cosmos DB skill — the one focused on **real application architecture** rather than raw SDK method calls.

If you just need basic CRUD reference, the lower-level `azure-cosmos-py` skill is available upstream. Most teams benefit far more from the patterns in `azure-cosmos-db-py`.

## Installation (within devpack or dependent projects)

```bash
apm install ./plugins/azure-cosmos --target agent-skills
```

After installation, the skill will be available in `.agents/skills/azure-cosmos-db-py`.

## Usage Tips

- Pair this with `azure-infrastructure-architecture` when setting up the surrounding Azure resources (Bicep, Container Apps, etc.).
- The skill strongly emphasizes `DefaultAzureCredential` + context managers — follow this for security and portability.
- Use the templates in `assets/` as starting points for new services.
- Read the `references/` files for deep dives (especially `partitioning.md` and `service-layer.md`).

## Attribution

All skill content is sourced from Microsoft and remains under the original license (MIT).

Original source: https://github.com/microsoft/skills

## Related Plugins in This Pack

- `azure-infrastructure-architecture` — Bicep, AKS, Well-Architected guidance (great companion when provisioning Cosmos accounts)
- `microsoft-foundry-agents` + `microsoft-agent-framework` — When your app also uses Azure AI Foundry

## Future Improvements

- Add the TypeScript Cosmos patterns skill (`azure-cosmos-ts`) if demand appears.
- Consider a small companion for the ARM management skill (`azure-resource-manager-cosmosdb-dotnet`) for infrastructure teams.

Contributions and requests for additional Cosmos DB coverage are welcome.