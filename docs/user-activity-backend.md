# User Activity Backend Spike

This branch adds a minimal persistence foundation for student activity.

## Local Database

By default the app uses SQLite at:

```text
instance/web_clases_rocedg.sqlite
```

The `instance/` folder is ignored by Git so local activity data is not committed.

To create the tables locally:

```powershell
$env:FLASK_APP = "app"
.\.venv\Scripts\python.exe -m flask init-db
```

## Production Configuration

Set `DATABASE_URL` to use a production database later. The configuration accepts
PostgreSQL-compatible URLs and normalizes legacy `postgres://` URLs to
`postgresql://`.

## What Is Tracked Now

- Generic activity events.
- Topic PDF open/download clicks routed through Flask.
- Resource open/download clicks for summaries, exams, quiz question PDFs, and
  solution PDFs when the template link uses the tracked route.
- Quiz starts.
- Quiz submissions with correct count, total question count, percentage score,
  and approximate duration when a start time is present in the session.

## What Is Not Tracked Yet

- Exact PDF page views.
- Whether a browser fully downloads or reads a static PDF after redirect.
- Activity from direct static-file URLs that bypass Flask.
- Real recommendations or advanced analytics.
- Teacher dashboards.
- A normalized user table. Current records are associated by session username.

## Maintenance Notes

This spike does not add migrations. If the model is approved, add migrations
before relying on schema changes in production.
