# Seattle Activities Skill

Use this skill whenever the user asks for things to do in Seattle.

## Behavior

1. Ask one brief clarifying question only if date, budget, or vibe is missing.
2. Prefer neighborhood-specific recommendations over city-wide generic lists.
3. Keep suggestions practical: include one-line why it fits.
4. If weather is mentioned or uncertain, call `get_seattle_weather` first.
5. For each recommendation set, include:
   - 1 low-cost option
   - 1 indoor fallback
   - 1 signature Seattle activity

## Output format

- Start with a short summary sentence.
- Then give exactly 3 options.
- End with one follow-up prompt asking if the user wants food-focused, outdoors-focused, or family-friendly ideas.
