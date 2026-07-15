---
name: seattle-activities
description: Suggest Seattle activities by neighborhood and vibe. Use when users ask what to do in Seattle, where to spend an evening, or how to plan nearby activities.
---

Use this skill for activity-planning requests in Seattle.

## Workflow

1. If missing, ask one short clarifying question for date, budget, or vibe.
2. If weather could affect choices, call `get_seattle_weather`.
3. Call `read_skill_resource` for `references/activity-options.md` and choose options that fit the user intent.
4. Personalize choices using `get_neighborhood_tip` when neighborhood guidance helps.

## Output rules

- Keep the response concise.
- Give exactly 3 activity options.
- Include at least:
  - 1 low-cost option
  - 1 indoor fallback
  - 1 iconic Seattle option
- End with one follow-up asking whether the user wants food-focused, outdoors-focused, or family-friendly ideas.
