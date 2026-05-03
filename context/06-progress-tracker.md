# Progress Tracker

## Current Phase

Exercise system planning / interactive practice design.

## Completed

- Site redesign and consolidation.
- Local run scripts and smoke tests.
- Project context system.
- Initial decision: exercises will become interactive guided pages, not just PDFs.

## In Progress

- Specification of LaTeX/PDF/interactive exercise system.

## Next Recommended Work

1. Create content skeleton.
2. Build induction pilot with 3-5 exercises.
3. Validate LaTeX format and compact PDF style.
4. Build `/practice` MVP.
5. Build `/exercise/<id>` MVP.

## Decisions

- Keep Flask/Jinja/JSON for now.
- Use `content/` as editable source.
- Use `static/` as public generated output.
- Use LaTeX source + pre-generated PDF.
- Do not compile LaTeX on Render.
- Exercise page will include PDF plus interactive panel.
- First supported interactions should be `single_choice` and `numeric`.
- Tracking is future work.

## Risks

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
