# Progress Tracker

## Current Phase

User activity backend persistence spike.

## Completed

- Site redesign and consolidation.
- Local run scripts and smoke tests.
- Project context system.
- Initial decision: exercises will become interactive guided pages, not just PDFs.
- Exercise system stack/spec documented.
- First content skeleton branch started.
- Decision: user activity needs real persistence.

## In Progress

- Minimal database foundation.
- Activity event log.
- Topic/resource access tracking.
- Quiz attempt tracking.

## Next Recommended Work

1. Review backend spike.
2. Decide whether to merge.
3. Later: add migrations.
4. Later: replace hardcoded users.
5. Later: connect progress UI to real data.
6. Later: implement exercise attempts for the new exercise system.

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
- Use SQLAlchemy/Flask-SQLAlchemy for the persistence spike.
- Use SQLite locally by default.
- Keep `DATABASE_URL` PostgreSQL-ready for production later.
- Store PDF/image paths and metadata only, not files.
- Do not refactor authentication yet; associate activity by session username.
- Do not build the full dashboard yet.

## Limitations

- Exact PDF page tracking requires a controlled PDF viewer later.
- Direct static file downloads are not trackable unless users enter through a Flask route.
- The current tracked resource route records open/download clicks before redirecting to static files.
- Current hardcoded users are associated by username only.

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
- 2026-09-06: Started `dev/user-activity-backend-spike` from latest `main` to add a minimal SQLAlchemy persistence foundation for activity events, topic/resource access, quiz attempts, and a simple real-data `/progress` page. No auth refactor, teacher dashboard, recommendation engine, PDF viewer, or exercise-system expansion is included.
