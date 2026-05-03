# Progress Tracker

## Current Phase

Post-redesign consolidation.

## Completed

- Repository history cleaned.
- Visual/site structure redesign merged to `main`.
- Executive documentation added to `main`.
- Local launch scripts and smoke tests branch created and pushed, pending merge unless already merged.
- Generated local/cache artifact cleanup branch created.
- Executive code documentation refreshed on `main`.

## In Progress

- Next focused product unit selection.

## Next Recommended Work

1. Review and understand the current structure.
2. Confirm local scripts and smoke tests remain healthy after future merges.
3. Plan the next product unit with a focused feature spec.
4. Keep documentation and progress notes current after each completed unit.

## Decisions

- Keep Flask.
- Keep Jinja templates.
- Keep JSON for now.
- Do not add a database yet.
- Use small branches and PRs.
- Use specs before Codex implements changes.
- Keep Render compatibility.
- Keep the app understandable for a non-expert maintainer.

## Risks

- Maintainer losing understanding due to too many AI-generated changes.
- Overengineering too early.
- Mixing product changes with architecture changes.
- Accidentally changing app behavior during documentation or tooling tasks.
- Adding a database before the product model is clear.

## Update Log

- 2026-05-03: Created initial project context system on `dev/project-context-system`.
- 2026-05-03: Cleaned generated local/cache artifacts and expanded `.gitignore` on `dev/cleanup-local-artifacts`.
- 2026-05-03: Refreshed executive code documentation and regenerated the PDF on `main`.
