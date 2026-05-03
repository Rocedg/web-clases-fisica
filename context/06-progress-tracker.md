# Progress Tracker

## Current Phase

Exercise content skeleton implementation.

## Completed

- Site redesign and consolidation.
- Local run scripts and smoke tests.
- Project context system.
- Initial decision: exercises will become interactive guided pages, not just PDFs.
- Exercise system stack/spec documented.
- First content skeleton branch started.

## In Progress

- Adding `content/exercises/` structure.
- Adding initial Faraday-Lenz pilot metadata.
- Adding validation/index scripts.

## Next Recommended Work

1. Fill real LaTeX for the first pilot exercise.
2. Generate first manual PDF.
3. Add first public asset.
4. Then create `/practice` MVP.

## Decisions

- Keep Flask/Jinja/JSON for now.
- Keep current quiz/homework behavior untouched.
- Use `content/` as editable source.
- Use `static/` as public generated output.
- Introduce `data/exercises.json` as future index.
- Use LaTeX source + pre-generated PDF.
- Do not compile LaTeX on Render.
- Exercise page will include PDF plus interactive panel.
- First supported interactions should be `single_choice` and `numeric`.
- Validate metadata before UI work.
- Do not build UI until skeleton and pilot data are stable.
- Tracking is future work.

## Risks

- Too much structure too early.
- Metadata becoming too complex.
- Paths becoming inconsistent.
- Creating planned exercises without later validating actual files.
- Overengineering too early.
- Importing too many exercises before validating the model.
- Copyright/source management becoming messy.
- Maintaining duplicate source/public files without automation.
- Losing project owner understanding if Codex changes too much at once.

## Update Log

- 2026-05-03: Created initial project context system on `dev/project-context-system`.
- 2026-05-03: Cleaned generated local/cache artifacts and expanded `.gitignore` on `dev/cleanup-local-artifacts`.
- 2026-05-03: Refreshed executive code documentation and regenerated the PDF on `main`.
- 2026-05-03: Documented the future interactive exercise system on `dev/exercise-system-spec`.
- 2026-05-03: Started exercise content skeleton work on `dev/exercise-content-skeleton`.
