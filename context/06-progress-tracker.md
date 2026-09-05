# Progress Tracker

## Current Phase

Processing first exercise source document.

## Completed

- Site redesign and consolidation.
- Local run scripts and smoke tests.
- Project context system.
- Initial decision: exercises will become interactive guided pages, not just PDFs.
- Exercise system stack/spec documented.
- First content skeleton branch started.
- Controlled source intake workflow added before converting PDFs into exercise metadata.
- First induction source PDF moved from `unchecked` to `processing`.
- Initial intake record and candidate map created for the first source PDF.

## In Progress

- Reviewing candidate exercises from the first induction source PDF.
- Keeping source material internal while planning adapted public exercises.

## Next Recommended Work

1. Review the first source candidate map.
2. Decide whether the extra field-B candidate should become a planned exercise.
3. Fill real LaTeX for the first pilot exercise.
4. Generate first manual PDF.
5. Add first public asset.
6. Then create `/practice` MVP.

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
- Copying source wording or figures directly into public exercise assets.
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
- 2026-05-03: Moved the first induction source PDF to processing and drafted its candidate map.

- 2026-09-05: Began UI redesign foundation work on branch `dev/ui-redesign-foundation` — updated templates and CSS tokens to the "Web Clases Rocedg" visual system (brand, colors, layout, responsive rules). No backend or exercise-system changes were made.
