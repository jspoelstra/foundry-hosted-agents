---
name: web-artifacts-builder
description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
license: Complete terms in LICENSE.txt
source: https://github.com/anthropics/skills
---

# Web Artifacts Builder

To build powerful frontend claude.ai artifacts, follow these steps:
1. Initialize the frontend repo using the init script
2. Develop your artifact by editing the generated code
3. Bundle all code into a single HTML file
4. Display artifact to user

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Design & Style Guidelines

VERY IMPORTANT: To avoid what is often referred to as "AI slop", avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project (adapt the script name as needed for this pack).

This creates a fully configured project with:
- React + TypeScript (via Vite)
- Tailwind CSS with shadcn/ui theming system
- Path aliases configured
- Many shadcn/ui components pre-installed
- All Radix UI dependencies included

### Step 2: Develop Your Artifact

Edit the generated files. Focus on real functionality and the aesthetic direction from the frontend-design skill when applicable.

### Step 3: Bundle to Single HTML File

Bundle the React app into a single HTML artifact for sharing.

This creates a self-contained artifact with all JavaScript, CSS, and dependencies inlined.

## Reference

- shadcn/ui components: https://ui.shadcn.com/docs/components

Combine this skill with `frontend-design` for the best results on complex React frontends.