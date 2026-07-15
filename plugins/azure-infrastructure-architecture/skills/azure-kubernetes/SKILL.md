---
name: azure-kubernetes
description: Production guidance for Azure Kubernetes Service (AKS). Covers networking (CNI), security, autoscaling, upgrades, GPU/AI workloads, egress, and Day-0 production checklists.
license: MIT
source: https://github.com/microsoft/skills
---

# Azure Kubernetes Service (AKS)

Expert guidance for running production workloads on AKS.

## Core Topics

- SKU selection (Automatic vs Standard)
- Networking (Azure CNI, Calico, network policies)
- Security and identity (Workload Identity, secrets, private clusters)
- Autoscaling (HPA, KEDA, Cluster Autoscaler)
- Upgrades and node pools
- GPU and AI/ML workloads
- Observability (Azure Monitor, Prometheus, Grafana)
- Egress and cost control
- Day-0 production readiness checklist

## When to Use

Any conversation involving AKS, Kubernetes on Azure, or container orchestration at scale.

Strongly recommended to combine with `azure-prepare` (for Bicep generation) and `cloud-solution-architect` (for overall design).