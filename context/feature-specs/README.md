# Feature Specs

Future feature work should get its own spec file before implementation.

Specs keep Codex and human maintainers aligned before code changes begin. They also reduce the risk of accidentally mixing product, architecture, UI, and testing changes in one branch.

## How to Create a Spec

1. Create a new Markdown file in `context/feature-specs/`.
2. Use a clear filename, for example `progress-tracking-v1.md`.
3. Fill in the template below.
4. Review scope before implementation starts.
5. Keep implementation branches small.

## Template

```md
# Feature name

## Goal

What problem does this solve?

## User-facing behavior

What should the student or maintainer see or be able to do?

## Files likely to change

- `app.py`
- `templates/...`
- `static/css/...`
- `data/...`
- `tests/...`

Adjust this list for the specific feature.

## Out of scope

What should not be changed in this feature?

## Implementation notes

Important technical details, constraints, or sequencing.

## Validation checklist

- [ ] App imports successfully.
- [ ] Relevant routes return expected status codes.
- [ ] JSON files load successfully.
- [ ] Templates render without crashing.
- [ ] Pytest passes, if code changed.
- [ ] Manual local run checked, if UI changed.

## Rollback notes

How can this feature be reverted safely if needed?
```

## Guidance

- Each future feature should get its own spec file before implementation.
- Do not use one spec for several unrelated features.
- Keep specs practical and short enough to maintain.
- Update `context/06-progress-tracker.md` when a feature unit is completed.

