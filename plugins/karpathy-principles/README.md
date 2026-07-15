# karpathy-principles

Karpathy-inspired behavioral guidelines for AI coding agents.

This APM plugin packages the widely popular four principles (originally shared as a `CLAUDE.md` template and promoted heavily on X) into a reusable, installable unit that works across Grok, GitHub Copilot, Claude, Cursor, and other agents.

## Principles

1. **Think Before Coding** — State assumptions, surface tradeoffs, ask clarifying questions.
2. **Simplicity First** — Minimum code that solves the problem. No speculative features or abstractions.
3. **Surgical Changes** — Only edit what the request requires. Never do drive-by refactors.
4. **Goal-Driven Execution** — Define verifiable success criteria and loop until they are met.

These rules dramatically reduce over-engineering, hallucinated requirements, and noisy diffs.

## What This Plugin Provides

- `skills/karpathy-principles/SKILL.md` — A first-class skill that can be activated via `/skills karpathy-principles` or auto-invoked. Enforces the discipline during sessions.
- `templates/AGENTS.md` — The canonical instruction file to drop at the root of any project.
- `templates/copilot-instructions.md` — Ready-to-use file for GitHub Copilot in VSCode.

## Installation (as part of devpack)

This plugin is authored inside the `devpack` APM project.

```bash
# From a project that depends on devpack (or directly in devpack itself)
apm install ./plugins/karpathy-principles --target agent-skills
```

Or, once published to a marketplace:

```bash
apm install karpathy-principles@devpack
```

After installation the skill becomes available in `.agents/skills/karpathy-principles/`.

## Adoption in a New Project

1. Copy `templates/AGENTS.md` → `AGENTS.md` (project root)
2. Optionally copy the copilot variant to `.github/copilot-instructions.md`
3. Install the skill via APM for persistent enforcement
4. Reference the principles in your own project README or AGENTS.md

## Source & Inspiration

The principles originate from Andrej Karpathy's public observations on effective LLM coding workflows. The popular original template was widely shared via repositories such as:

- https://github.com/multica-ai/andrej-karpathy-skills
- https://github.com/forrestchang/andrej-karpathy-skills

This packaged version generalizes the file naming and framing for multi-tool environments (especially Grok + GitHub Copilot + VSCode users) while preserving the original intent and wording of the four rules.

## License

MIT (same as the plugin manifests). The guidelines themselves are inspired by public commentary and are intended for broad reuse.