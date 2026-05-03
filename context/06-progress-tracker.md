# Progress Tracker

## Current Phase

Post-redesign consolidation.

## Completed

- Repository history cleaned.
- Visual/site structure redesign merged to `main`.
- Executive documentation added to `main`.
- Local launch scripts and smoke tests branch created and pushed, pending merge unless already merged.

## In Progress

- Project context system.

## Next Recommended Work

1. Review and understand the current structure.
2. Merge the local-run/tests branch if it has not already been merged.
3. Add and review the context system.
4. Then plan the next product unit with a focused feature spec.

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

