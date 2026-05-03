"""Build data/exercises.json from topic-level exercise metadata.

This first builder only creates the future /practice summary index. It does not
compile LaTeX, copy assets, or generate PDFs.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SUMMARY_FIELDS = [
    "id",
    "title",
    "course",
    "block",
    "topic",
    "concept",
    "exercise_type",
    "subtype",
    "difficulty",
    "estimated_time_min",
    "statement_pdf",
    "solution_pdf",
    "tags",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def topic_files(root: Path) -> list[Path]:
    content_root = root / "content" / "exercises"
    if not content_root.exists():
        return []
    return sorted(content_root.rglob("exercises.json"))


def summarize_exercise(exercise: dict[str, Any]) -> dict[str, Any]:
    summary = {field: exercise.get(field) for field in SUMMARY_FIELDS}
    workflow = exercise.get("workflow") if isinstance(exercise.get("workflow"), dict) else {}
    summary["workflow"] = {
        "status": workflow.get("status")
    }
    return summary


def collect_exercises(root: Path) -> list[dict[str, Any]]:
    exercises: list[dict[str, Any]] = []
    for path in topic_files(root):
        data = load_json(path)
        for exercise in data.get("exercises", []):
            if isinstance(exercise, dict):
                exercises.append(summarize_exercise(exercise))
    return exercises


def build_index(root: Path | None = None, write: bool = True) -> dict[str, Any]:
    root = root or repo_root()
    exercises = collect_exercises(root)
    index = {
        "version": 1,
        "generated": True,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source": "content/exercises",
        "exercises": exercises,
    }

    if write:
        output_path = root / "data" / "exercises.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(index, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    return index


def main() -> int:
    root = repo_root()
    files = topic_files(root)
    print("Building exercise index...")
    print(f"Found {len(files)} topic exercise file{'s' if len(files) != 1 else ''}.")
    index = build_index(root)
    print(f"Wrote data/exercises.json with {len(index['exercises'])} exercises.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
