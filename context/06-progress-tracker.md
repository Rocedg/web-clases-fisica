# Progress Tracker

## Current Phase

Exercise source intake workflow implementation.

## Completed

- Site redesign and consolidation.
- Local run scripts and smoke tests.
- Project context system.
- Initial decision: exercises will become interactive guided pages, not just PDFs.
- Exercise system stack/spec documented.
- First content skeleton branch started.
- Controlled source intake workflow added before converting PDFs into exercise metadata.

## In Progress

- Defining intake states for unchecked, processing, and checked source documents.
- Adding templates for source records and candidate exercise maps.

## Next Recommended Work

1. Use the intake workflow on the first source PDF.
2. Fill real LaTeX for the first pilot exercise.
3. Generate first manual PDF.
4. Add first public asset.
5. Then create `/practice` MVP.

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
- Use `content/intake/` as a controlled workflow before turning source PDFs into exercise metadata.
- Treat source PDFs as internal references, not public final assets.
- Public exercises should use adapted wording and recreated or cleaned figures where needed.
- Tracking is future work.

## Risks

- Too much structure too early.
- Metadata becoming too complex.
- Paths becoming inconsistent.
- Creating planned exercises without later validating actual files.
- Converting PDFs into exercises before source review is complete.
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
- 2026-05-03: Added controlled exercise source intake workflow on `dev/exercise-source-intake`.
