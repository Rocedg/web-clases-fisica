# Project Overview

## Product

Rocedg Física Bach is a guided Physics study platform for Bachillerato students. It gives students structured access to topics, summaries, exercises/quizzes, exams, homework, and additional PAU/selectividad-related information.

The app is intentionally lightweight. It uses Flask, Jinja templates, static CSS, static PDFs, and JSON data files. It does not use a database yet.

## Users

- Students who need guided physics practice.
- The teacher/maintainer who organizes materials and eventually wants progress tracking.
- Guest/demo users for testing.

## Core User Flows

1. A student opens the home page and chooses a study section.
2. A student logs in to access protected study materials.
3. A student reviews topic PDFs.
4. A student practices quizzes and receives immediate results.
5. A student opens exam and PAU/selectividad resources.
6. The maintainer adds or updates PDF references through JSON and templates.
7. A demo user signs in with guest credentials to verify the experience.

## Current Product Scope

In scope now:

- Flask app.
- Static PDFs.
- JSON-driven content.
- Clear navigation.
- Login-based protected sections.
- Local testing workflow.
- Render deployment.

## Explicitly Out of Scope

Out of scope for now:

- Database.
- Student progress tracking.
- PostgreSQL.
- React/Next.js migration.
- AI-generated exercises inside the app.
- Payment/subscription features.
- Real-time collaboration.
- Complex admin dashboard.

## Success Criteria

The product is successful in its current phase if:

- Students can quickly find notes, exercises, exams, and PAU information.
- The maintainer can understand the project structure without specialist knowledge.
- The app runs locally on Windows with simple commands or helper scripts.
- The app remains deployable on Render with `gunicorn app:app`.
- JSON content can be updated without introducing a database.
- Future AI-assisted work is guided by explicit context and small specs.

