# Progress Tracker

## Current Phase

UI redesign foundation cleanup and review preparation.

## Completed

- Repository history cleaned.
- Visual/site structure redesign merged to `main`.
- Executive documentation added to `main`.
- Local launch scripts and smoke tests branch created and pushed, pending merge unless already merged.
- Generated local/cache artifact cleanup branch created.
- Executive code documentation refreshed on `main`.
- UI redesign foundation started on `dev/ui-redesign-foundation`.

## In Progress

- Completing UI-only cleanup and polish for `dev/ui-redesign-foundation`.

## Next Recommended Work

1. Review the UI redesign branch diff before merge.
2. Verify the app in browser across desktop and mobile widths.
3. Merge only after confirming the branch contains no exercise-system artifacts.
4. Plan future exercise-system work in a separate branch/spec.

## Decisions

- Keep Flask.
- Keep Jinja templates.
- Keep JSON for now.
- Do not add a database yet.
- Use small branches and PRs.
- Use specs before Codex implements changes.
- Keep Render compatibility.
- Keep the app understandable for a non-expert maintainer.
- Keep UI redesign work visual-only; no new routes or exercise backend in this branch.
- Use `Web Clases Rocedg` as the brand name, with `Física` as a subject pill.

## Risks

- Maintainer losing understanding due to too many AI-generated changes.
- Overengineering too early.
- Mixing UI polish with future exercise-system/backend changes.
- Accidentally changing app behavior during documentation or tooling tasks.
- Adding a database before the product model is clear.
- Letting old design reference locations or placeholder branding leak into review.

## Update Log

- 2026-05-03: Created initial project context system on `dev/project-context-system`.
- 2026-05-03: Cleaned generated local/cache artifacts and expanded `.gitignore` on `dev/cleanup-local-artifacts`.
- 2026-05-03: Refreshed executive code documentation and regenerated the PDF on `main`.
- 2026-09-05: Began UI redesign foundation work on branch `dev/ui-redesign-foundation` - updated templates and CSS tokens to the "Web Clases Rocedg" visual system (brand, colors, layout, responsive rules). No backend or exercise-system changes were made.
- 2026-09-05: Cleaned the UI redesign branch scope by removing exercise/intake/backend artifacts, moving design references under `docs/design/ui-redesign-reference/`, adding the real logo as a static brand asset, and polishing existing templates/CSS. No route, data model, dependency, or authentication changes were made.
- 2026-09-05: Refined the home dashboard structure with a compact welcome panel, four real-count metric cards, a prominent illustrative route recommendation, four direct-access cards, and three recommended-practice cards. No backend, route, data, dependency, or authentication changes were made.
- 2026-09-06: Replaced the top-level PAU navigation item with a visual-only Progreso area, added a protected `/progress` mock page, moved summary resources into the Apuntes page presentation, and kept `/miscellaneous` available without promoting it in main navigation. No database, persistence, data-file, exercise-system, or dependency changes were made.
