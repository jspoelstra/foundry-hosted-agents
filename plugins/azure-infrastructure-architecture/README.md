# azure-infrastructure-architecture

Curated high-signal skills for Azure infrastructure, Bicep, containers, and solution architecture.

**Primary Source:** https://github.com/microsoft/skills (azure-skills plugin)

## Included Skills

- **cloud-solution-architect** — Turns the agent into a Cloud Solution Architect. Covers the Well-Architected Framework, architecture styles, design patterns, technology selection, and mission-critical design.

- **azure-prepare** — The main IaC skill. Generates Bicep (or Terraform), azure.yaml, Dockerfiles, and deployment plans. Excellent for Container Apps, AKS, and app-centric infrastructure.

- **azure-kubernetes** — Production guidance for AKS (networking, security, autoscaling, GPU workloads, Day-0 checklists, etc.).

## Usage

After installing via APM, the skills are available via `/skills cloud-solution-architect`, etc.

These pair extremely well with the `microsoft-foundry-agents` plugin when you're building agent workloads on Azure.

## Recommendations

- Use `azure-prepare` early in any infrastructure conversation.
- Combine `cloud-solution-architect` for reviews and high-level decisions.
- Reach for `azure-kubernetes` when the solution involves AKS.

Additional skills (azure-deploy, azure-validate, more specific Bicep patterns, Azure AI Search SDK skills, etc.) can be added on request.