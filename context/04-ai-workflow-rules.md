# AI Workflow Rules

## Start Here

Every Codex or AI coding session should begin by reading:

- `AGENTS.md`
- All files in `context/`
- The relevant feature spec, if one exists.

## Standard Workflow

1. Restate the task scope.
2. Identify affected files.
3. Ask for approval before broad changes.
4. Implement one unit at a time.
5. Do not mix unrelated changes.
6. Prefer small pull requests.
7. Update `context/06-progress-tracker.md` after completing a unit.
8. Run validation.
9. Report what changed.
10. Report validation results and any follow-up risks.

## Scope Discipline

Do not make hidden assumptions about product direction.

Examples:

- Do not add a database just because progress tracking is mentioned.
- Do not migrate UI to React because a component feels complex.
- Do not redesign pages during a testing task.
- Do not change login behavior during documentation work.

## Approval Required

Ask for explicit approval before:

- Changing architecture.
- Adding a database.
- Introducing new frameworks.
- Changing deployment assumptions.
- Changing protected route behavior.
- Reorganizing large folder structures.
- Making broad visual redesigns.

## Good Prompts for This Project

Good:

```text
Add smoke tests for the current Flask routes without changing app behavior.
```

Good:

```text
Create a JSON spec for future progress tracking, but do not implement the database yet.
```

Good:

```text
Improve the topics page using the existing CSS system and Jinja templates only.
```

Good:

```text
Document how Render deployment works and verify gunicorn app:app still applies.
```

## Bad Prompts for This Project

Bad:

```text
Rebuild this app in React and add a PostgreSQL database.
```

Why bad:

- It violates current scope and architecture.

Bad:

```text
Make it more modern; change anything you want.
```

Why bad:

- Too broad and likely to mix unrelated changes.

Bad:

```text
Add progress tracking and redesign the whole dashboard in one PR.
```

Why bad:

- Mixes product behavior, data architecture, and UI redesign.

Bad:

```text
Fix tests and clean up all templates while you are there.
```

Why bad:

- Encourages unrelated cleanup.

## Pull Request Expectations

Prefer small PRs with:

- Clear title.
- Scope summary.
- Files changed.
- Validation results.
- Risks or follow-up items.

