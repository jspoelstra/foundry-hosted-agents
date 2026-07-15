---
name: foundry-models
description: Discover, deploy, and manage models on Microsoft AI Foundry. Supports preset deployments, fully customized deployments (SKU, capacity, RAI), capacity discovery across regions, and quota management.
license: MIT
metadata:
  author: Microsoft (curated)
  source: https://github.com/microsoft/skills
---

# Foundry Models

Covers the model side of Foundry:

- Model catalog discovery
- Quick preset deployments
- Advanced custom deployments (version, SKU, capacity, content filters)
- Capacity and quota checking
- Regional availability

**Tip:** Start with the `microsoft-foundry` router skill — it intelligently routes model-related requests to the best sub-skill (`models/deploy-model` and related).