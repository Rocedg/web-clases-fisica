# Architecture

## Current Folder Structure

```text
.
├── app.py
├── data/
├── docs/
├── static/
│   ├── css/
│   └── pdfs/
├── templates/
├── tests/
├── AGENTS.md
├── README.md
├── requirements.txt
└── local run scripts, when present
```

## `app.py`

`app.py` is the Flask entry point. It defines:

- The Flask `app` object.
- Session/login helpers.
- JSON loading helpers.
- Template context helpers.
- Routes for home, login, topics, homework, quizzes, PAU information, exams, and errors.

Render depends on this invariant:

```text
gunicorn app:app
```

Do not rename the Flask object or move it without a dedicated architecture spec.

## `templates/`

`templates/` contains Jinja templates. The site uses server-rendered HTML, not a client-side framework.

Important roles:

- `base.html` provides the shared layout.
- `home.html` provides the study dashboard.
- `templates/user/` contains student-facing pages.
- `templates/errors/` contains error pages.
- `templates/components/` contains reusable Jinja macros.

## `static/css/`

CSS is split by responsibility:

- `tokens.css`: design variables.
- `layout.css`: global layout, navigation, footer.
- `components.css`: reusable cards, buttons, panels, forms.
- `pages.css`: page-specific layout.
- `responsive.css`: responsive behavior.
- `style.css`: main import file.

Future CSS changes should extend this structure instead of creating unrelated one-off styles.

## `static/pdfs/`

PDFs are static learning assets. JSON files often reference these PDFs.

Do not move PDFs without updating JSON references and validating links.

## `data/*.json`

JSON files are the current content layer. They replace the need for a database at this stage.

Current responsibilities:

- `topics.json`: topic PDF metadata.
- `quizzes.json`: quiz metadata, answer keys, question/solution PDFs.
- `exams.json`: exam and PAU practice metadata.
- `summaries.json`: summary PDF metadata.

Keep JSON formatting readable and stable.

## `tests/`

`tests/` contains basic pytest smoke tests when present. These tests should remain simple and robust.

Expected coverage:

- App imports.
- Public routes respond.
- Protected routes redirect or deny access.
- JSON files load.
- Main templates render without server errors.

## Local Run Scripts

Local helper scripts may exist:

- `start-web.bat`
- `run-local.ps1`
- `setup-local.ps1`

They are intended for a non-technical Windows user. Keep messages clear and avoid requiring advanced shell knowledge.

## Render Deployment Assumptions

- Python dependencies are declared in `requirements.txt`.
- The app can be served by `gunicorn app:app`.
- No database service is required yet.
- Static assets are served from the Flask project.
- Environment variable `SECRET_KEY` can be set in production.

## Architectural Invariants

- Keep Flask as the framework.
- Keep Jinja templates.
- Keep JSON content for now.
- Do not add a database without a dedicated spec.
- Do not move PDFs without updating JSON references.
- Do not change authentication/protected route behavior without explaining it.
- Keep `gunicorn app:app` working for Render.
- Keep local launch scripts working on Windows.
- Keep the project simple and maintainable.

