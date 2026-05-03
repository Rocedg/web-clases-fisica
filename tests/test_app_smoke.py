import json
from pathlib import Path

from app import app as flask_app


def test_app_imports_successfully():
    assert flask_app is not None
    assert flask_app.name == "app"


def test_home_returns_200():
    client = flask_app.test_client()
    response = client.get("/")

    assert response.status_code == 200


def test_login_returns_200():
    client = flask_app.test_client()
    response = client.get("/login")

    assert response.status_code == 200


def test_topics_requires_login():
    client = flask_app.test_client()
    response = client.get("/topics")

    assert response.status_code in {302, 401, 403}
    if response.status_code == 302:
        assert "/login" in response.headers["Location"]


def test_homework_requires_login():
    client = flask_app.test_client()
    response = client.get("/homework")

    assert response.status_code in {302, 401, 403}
    if response.status_code == 302:
        assert "/login" in response.headers["Location"]


def test_exams_currently_public():
    client = flask_app.test_client()
    response = client.get("/exams")

    assert response.status_code == 200


def test_json_files_load_successfully():
    data_dir = Path("data")

    for json_file in data_dir.glob("*.json"):
        with json_file.open(encoding="utf-8") as file:
            assert json.load(file) is not None


def test_main_template_rendering_does_not_crash():
    client = flask_app.test_client()

    public_paths = ["/", "/login", "/exams"]
    for path in public_paths:
        response = client.get(path)
        assert response.status_code < 500

    client.post(
        "/login",
        data={"username": "Guest", "password": "studentpass"},
        follow_redirects=False,
    )

    protected_paths = ["/topics", "/homework", "/miscellaneous"]
    for path in protected_paths:
        response = client.get(path)
        assert response.status_code < 500
