# UI Context

## Current Direction

The UI should feel like a clear academic study platform: modern, calm, readable, and confidence-building.

It should guide the student toward useful actions:

- Start with notes.
- Practice exercises.
- Review exams.
- Consult PAU/selectividad information.

The site should not feel flashy, noisy, or overly experimental.

## Visual Principles

- Prioritize readability.
- Use clear hierarchy.
- Make cards and sections easy to scan.
- Use consistent buttons.
- Keep spacing comfortable.
- Keep page structure predictable.
- Use friendly academic language.
- Help the student know what to do next.

## Existing CSS System

Respect the current CSS split:

- `tokens.css`
- `layout.css`
- `components.css`
- `pages.css`
- `responsive.css`
- `style.css`

Use `tokens.css` for design variables. Extend existing component classes before inventing new one-off styles.

## Existing Visual Identity

Keep the current redesign direction:

- Primary blue.
- Light background.
- Beige secondary-course accent.
- Rounded panels and cards.
- Clear navigation.
- Dashboard-style home page.
- Reusable resource cards.

Do not invent a completely new visual identity unless the user explicitly asks for a redesign spec.

## Future UI Changes

Future UI changes should:

- Extend existing cards, panels, badges, and buttons.
- Reuse macros where possible.
- Preserve mobile readability.
- Avoid unnecessary JavaScript.
- Avoid adding frontend frameworks.
- Keep Bootstrap usage compatible with the existing templates.

## UI Validation

For UI changes, check:

- Desktop layout.
- Mobile layout.
- Navigation clarity.
- Button consistency.
- PDF links.
- Login/protected route flow.
- No broken template rendering.

