---
name: foundry-hosted-agents
description: Build, deploy, and manage Microsoft AI Foundry hosted agents (containerized agents using Microsoft Agent Framework, LangGraph, or custom code). Covers Responses and Invocations protocols, Entra identity, endpoints, and deployment via azd.
license: MIT
metadata:
  author: Microsoft (curated)
  source: https://github.com/microsoft/skills
---

# Foundry Hosted Agents

This skill focuses on **hosted (code-based) agents** on Microsoft AI Foundry.

For the full router and complete set of sub-skills, load the `microsoft-foundry` skill first.

## Key Capabilities

- Creating new hosted agents (Python/.NET)
- Containerizing and deploying via ACR + azd
- Configuring Responses vs Invocations protocols
- Setting up Entra identities for agents
- Managing agent endpoints and versioning

**Recommended starting point:** Use the `microsoft-foundry` skill and ask for hosted agent workflows. It will guide you to the right sub-skill and mandatory pre-checks.

See the full `microsoft-foundry` skill for detailed workflows around `create` → `deploy` → `invoke`.