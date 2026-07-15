---
name: azure-prepare
description: Analyze requirements and generate modern Azure infrastructure using Bicep (preferred), azure.yaml, Dockerfiles, and deployment plans. Strong focus on Container Apps, AKS, and app-centric workloads.
license: MIT
source: https://github.com/microsoft/skills
---

# Azure Prepare (Bicep & IaC)

Primary skill for preparing Azure application infrastructure and deployments.

## Key Capabilities

- Generate high-quality Bicep modules and main.bicep files.
- Create azure.yaml for azd deployments.
- Produce Dockerfiles and containerization strategies.
- Recommend appropriate Azure services based on requirements (Container Apps vs AKS vs App Service, etc.).
- Generate deployment plans and .azure/deployment-plan.md artifacts.
- Handle common patterns: managed identity, Key Vault references, Application Insights, etc.

## Recommended Workflow

1. Understand the application and its non-functional requirements.
2. Choose architecture style and services.
3. Generate Bicep + supporting files.
4. Validate the plan with the user.
5. Hand off to `azure-deploy` or similar for actual deployment.

Prefer Bicep over Terraform unless the user explicitly requests otherwise.

This skill is especially powerful when combined with `cloud-solution-architect` for the "why" and `azure-kubernetes` when AKS is selected.