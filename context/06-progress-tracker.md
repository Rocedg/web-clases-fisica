# Progress Tracker

## Current Phase

T0 embedded lesson viewer pilot prepared for review on `dev/t0-lesson-pdf-pilot`.

## Completed

- Repository history cleaned.
- Visual/site structure redesign merged to `main`.
- Executive documentation added to `main`.
- Local launch scripts and smoke tests branch created and pushed, pending merge unless already merged.
- Generated local/cache artifact cleanup branch created.
- Executive code documentation refreshed on `main`.
- UI redesign foundation started on `dev/ui-redesign-foundation`.
- Exercise system stack/spec documented.
- First content skeleton branch merged to `main`.
- User activity backend persistence spike merged to `main`.
- UI redesign foundation merged to `main` with the activity backend preserved.
- T0 introductory lesson PDF pilot created, compiled, and connected to Apuntes with existing resource tracking.
- T0 lesson PDF open/download actions separated with explicit inline/attachment headers.
- T0 lesson viewer page added so students open the lesson inside the Web Clases Rocedg layout before downloading or practicing.
- T0 lesson PDF refined to v0.2 with a nine-page, one-column guided layout and updated app page-count metadata.
- T0 lesson PDF refined to v0.3 with four didactic blocks, expanded measurement-quality explanations, and a fuller calculus section.

## In Progress

- None.

## Next Recommended Work

1. Review the T0 v0.3 PDF and embedded lesson viewer in a browser before merging.
2. If approved, reuse this lesson style and page pattern for the next PDF one lesson at a time.
3. Later: add database migrations before relying on production schema changes.
4. Later: replace hardcoded users with a real user table.
5. Later: implement exercise attempts for the new exercise system.

## Decisions

- Keep Flask/Jinja templates.
- Keep JSON for learning content for now.
- Use small branches and PRs.
- Use specs before Codex implements changes.
- Keep Render compatibility.
- Keep the app understandable for a non-expert maintainer.
- Use `Web Clases Rocedg` as the brand name, with `Física` as a subject pill.
- Use SQLAlchemy/Flask-SQLAlchemy for the persistence spike.
- Use SQLite locally by default.
- Keep `DATABASE_URL` PostgreSQL-ready for production later.
- Store PDF/image paths and metadata only, not files.
- Do not refactor authentication yet; associate activity by session username.
- Do not build the full dashboard yet.
- Do not build the teacher dashboard yet.
- Do not expand the exercise system in the UI redesign update branch.

## Limitations

- Exact PDF page tracking requires a controlled PDF viewer later.
- Direct static file downloads are not trackable unless users enter through a Flask route.
- The current tracked resource route records open/download clicks before serving or redirecting resources.
- Current hardcoded users are associated by username only.
- Tracked PDF routes now serve local PDFs directly with explicit `Content-Disposition` and no-store cache headers.
- The T0 lesson viewer records `lesson_viewed` on `/lesson/T0-introduccion`, embeds the static PDF to avoid double-counting, and tracks downloads through `/resource/lesson_pdf/.../download`.

## Risks

- Maintainer losing understanding due to too many AI-generated changes.
- Overengineering too early.
- Mixing UI polish with future exercise-system/backend changes.
- Accidentally changing app behavior during documentation or tooling tasks.
- Adding a database before the product model is clear.
- Letting old design reference locations or placeholder branding leak into review.

## Update Log

- 2026-05-03: Created initial project context system on `dev/project-context-system`.
- 2026-05-03: Cleaned generated local/cache artifacts and expanded `.gitignore` on `dev/cleanup-local-artifacts`.
- 2026-05-03: Refreshed executive code documentation and regenerated the PDF on `main`.
- 2026-05-03: Documented the future interactive exercise system on `dev/exercise-system-spec`.
- 2026-05-03: Started exercise content skeleton work on `dev/exercise-content-skeleton`.
- 2026-09-05: Began UI redesign foundation work on branch `dev/ui-redesign-foundation` - updated templates and CSS tokens to the "Web Clases Rocedg" visual system (brand, colors, layout, responsive rules). No backend or exercise-system changes were made.
- 2026-09-05: Cleaned the UI redesign branch scope by removing exercise/intake/backend artifacts, moving design references under `docs/design/ui-redesign-reference/`, adding the real logo as a static brand asset, and polishing existing templates/CSS. No route, data model, dependency, or authentication changes were made.
- 2026-09-05: Refined the home dashboard structure with a compact welcome panel, four real-count metric cards, a prominent illustrative route recommendation, four direct-access cards, and three recommended-practice cards. No backend, route, data, dependency, or authentication changes were made.
- 2026-09-06: Replaced the top-level PAU navigation item with a visual-only Progreso area, added a protected `/progress` mock page, moved summary resources into the Apuntes page presentation, and kept `/miscellaneous` available without promoting it in main navigation. No database, persistence, data-file, exercise-system, or dependency changes were made.
- 2026-09-06: Started `dev/user-activity-backend-spike` from latest `main` to add a minimal SQLAlchemy persistence foundation for activity events, topic/resource access, quiz attempts, and a simple real-data `/progress` page. No auth refactor, teacher dashboard, recommendation engine, PDF viewer, or exercise-system expansion is included.
- 2026-09-06: Merged latest `main` into `dev/ui-redesign-foundation`, preserving the activity backend and restyling `/progress` so it shows real saved activity inside the UI redesign system. PAU remains available at `/miscellaneous` but is not a top-level navigation item.
- 2026-09-07: Merged `dev/ui-redesign-foundation` into `main` after final pytest, database initialization, local launch, and route checks. Existing exercise skeleton files from `main` were preserved without starting new exercise-system work.
- 2026-09-07: Started `dev/t0-lesson-pdf-pilot` from latest `main`; created a polished T0 introductory lesson PDF in LaTeX, exposed it on `/topics`, and reused the existing activity tracking route for lesson PDF open/download clicks.
- 2026-09-07: Fixed tracked PDF response behavior so open actions return explicit inline PDFs and download actions return explicit attachments, while preserving activity tracking and avoiding stale tracked-route caches.
- 2026-09-08: Added `/lesson/T0-introduccion` as an embedded Web Clases Rocedg lesson viewer, changed the T0 Apuntes primary action to `Ver lección`, kept tracked downloads, and validated lesson view/download events on `/progress`.
- 2026-09-08: Refined the T0 lesson PDF to v0.2: added an introductory page, changed the PDF to a nine-page one-column guided layout, redrew diagrams in TikZ, compiled the static lesson PDF, and updated the lesson page count.
- 2026-09-08: Refined the T0 lesson PDF to v0.3: reorganized the lesson into four didactic blocks, replaced the visual roadmap with a linked vertical index, updated page numbering to `Página X de Y`, expanded uncertainty and calculus explanations, recompiled the static PDF, and updated the lesson page count.
