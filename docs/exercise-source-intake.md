# Exercise Source Intake

This workflow controls how source documents enter the future exercise system before they become public exercise metadata, PDFs, or assets.

The goal is simple: keep original source PDFs separate from public final exercises. A source document is a reference for the maintainer. It is not the final public student-facing asset.

## Folder States

```text
content/intake/
  unchecked/
  processing/
  checked/
```

### `unchecked/`

Use this folder for newly added PDFs or source files that have not been reviewed yet.

Files here are not approved as exercise references. They may still need:

- Topic classification.
- Source/origin notes.
- Copyright review.
- Page-by-page inspection.
- Decision about whether figures should be recreated, cleaned, or ignored.

### `processing/`

Use this folder for documents currently being analysed.

At this stage, the maintainer or Codex can:

- Identify candidate exercises.
- Map source pages to future `target_exercise_id` values.
- Decide exercise type and subtype.
- Propose interactions such as `single_choice` or `numeric`.
- Decide a public asset strategy for figures and graphs.

Use `content/intake/intake-template.md` for document-level notes and `content/intake/candidate-map-template.json` when one source can produce several candidate exercises.

### `checked/`

Use this folder for documents that have been reviewed and approved as source references.

Checked means:

- The source is understood.
- Candidate exercises have been identified or intentionally rejected.
- Copyright/source risk has been reviewed at a practical project level.
- The document can be cited internally as a reference for future adapted exercises.

Checked does not mean the original PDF should be published as a public exercise.

## Source PDFs Are Internal References

Source PDFs in `content/intake/` are internal working references. They should not be treated as final public assets and should not be served directly by the website.

Future public exercises should use:

- Adapted wording.
- Project-owned LaTeX statements and solutions.
- Recreated or cleaned figures where needed.
- Public assets stored under `static/exercises/` only after review.

## Public Exercise Policy

When converting a source document into exercise metadata:

1. Keep the original PDF in the intake workflow as a reference.
2. Create a candidate map before adding real exercise metadata.
3. Rewrite the statement in the project's own wording.
4. Recreate simple diagrams as SVG when reasonable.
5. Clean or redraw figures instead of publishing third-party figures as-is when avoidable.
6. Store public PDFs and assets under `static/exercises/` only after they are reviewed.
7. Keep current quiz/homework behavior untouched unless a later migration plan says otherwise.

This is an operational content policy for the project, not legal advice.

## Recommended Intake Steps

1. Put a new source PDF in `content/intake/unchecked/`.
2. Create an intake note from `content/intake/intake-template.md`.
3. Move the source to `processing/` when analysis starts.
4. Create a candidate map from `content/intake/candidate-map-template.json`.
5. Decide which candidates are worth turning into exercises.
6. Move the source to `checked/` only after review.
7. Add or update exercise metadata in a separate focused branch.

Do not bulk-import large source documents directly into `content/exercises/`. The intake step exists to prevent messy sources, unclear rights, and unstable metadata.
