"""Validate the T0 v4 exercise-bank catalogue contract."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BANK_PATH = ROOT / "content" / "exercises" / "1bach" / "t0" / "exercises.json"

EXPECTED_DISTRIBUTION = {
    "units": 16,
    "vectors": 24,
    "measurement": 20,
    "calculus_graphs": 20,
}

RETIRED_IDS = {
    "t0_u_017",
    "t0_u_018",
    *{f"t0_v_{number:03d}" for number in range(25, 37)},
    "t0_e_001",
    "t0_e_002",
    *{f"t0_c_{number:03d}" for number in range(21, 25)},
}

MANDATORY_ASSET_IDS = {
    "t0_v_012",
    "t0_v_017",
    "t0_v_018",
    "t0_v_024",
    "t0_c_016",
    "t0_c_019",
    "t0_c_020",
}


def load_bank() -> dict[str, Any]:
    with BANK_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def validate_bank(root: Path | None = None) -> list[str]:
    root = root or ROOT
    errors: list[str] = []
    bank = load_bank()
    exercises = bank.get("exercises", [])
    ids = [exercise.get("id") for exercise in exercises]

    if len(exercises) != 80:
        errors.append(f"Expected 80 active T0 exercises, found {len(exercises)}.")
    duplicates = [exercise_id for exercise_id, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicated IDs: {', '.join(sorted(duplicates))}.")
    if Counter(exercise.get("family") for exercise in exercises) != EXPECTED_DISTRIBUTION:
        errors.append(f"Unexpected family distribution: {Counter(exercise.get('family') for exercise in exercises)}.")

    for exercise in exercises:
        exercise_id = str(exercise.get("id"))
        if exercise.get("version") != 4:
            errors.append(f"{exercise_id}: version must be 4.")
        if exercise.get("difficulty") == 1:
            errors.append(f"{exercise_id}: difficulty 1 is not allowed in active v4.")
        if exercise_id in RETIRED_IDS:
            errors.append(f"{exercise_id}: retired ID appears in active catalogue.")
        if "hints" not in exercise or not isinstance(exercise.get("hints"), list):
            errors.append(f"{exercise_id}: hints must be present as a list.")
        if not isinstance(exercise.get("solution"), dict) or not exercise["solution"].get("summary_steps"):
            errors.append(f"{exercise_id}: guided solution summary_steps are required.")

        fields = exercise.get("interactions") or exercise.get("response_fields") or []
        if not fields:
            errors.append(f"{exercise_id}: at least one response field is required.")
        for field in fields:
            field_id = field.get("id", "<missing>")
            field_type = field.get("type")
            if not field.get("required"):
                errors.append(f"{exercise_id}.{field_id}: required must be true.")
            if field_type == "numeric":
                if field.get("expected_value") is None:
                    errors.append(f"{exercise_id}.{field_id}: numeric field missing expected_value.")
                if field.get("tolerance") is None:
                    errors.append(f"{exercise_id}.{field_id}: numeric field missing tolerance.")
            if field_type == "single_choice":
                option_ids = [option.get("id") for option in field.get("options", [])]
                if not option_ids or field.get("correct_option_id") not in option_ids:
                    errors.append(f"{exercise_id}.{field_id}: single_choice needs stable options and correct_option_id.")

    for exercise_id in MANDATORY_ASSET_IDS:
        exercise = next((item for item in exercises if item.get("id") == exercise_id), None)
        if not exercise:
            errors.append(f"{exercise_id}: mandatory asset exercise missing.")
            continue
        if not exercise.get("assets"):
            errors.append(f"{exercise_id}: mandatory SVG asset not referenced.")
            continue
        for asset in exercise["assets"]:
            path = root / asset["path"]
            if not path.exists():
                errors.append(f"{exercise_id}: missing SVG asset {asset['path']}.")
                continue
            svg = path.read_text(encoding="utf-8")
            if "<svg" not in svg or "viewBox=" not in svg:
                errors.append(f"{exercise_id}: SVG must include <svg> and viewBox.")
            if "<title" not in svg or "<desc" not in svg:
                errors.append(f"{exercise_id}: SVG must include title and desc.")

    retired_metadata_ids = {item.get("id") for item in bank.get("retired_exercises", [])}
    missing_retired = RETIRED_IDS - retired_metadata_ids
    if missing_retired:
        errors.append(f"Missing retired metadata IDs: {', '.join(sorted(missing_retired))}.")

    return errors


def main() -> int:
    errors = validate_bank()
    if errors:
        print("T0 v4 catalogue validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("T0 v4 catalogue validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
