from pathlib import Path

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)
base_path = Path.cwd() / "test_rosters"
test_roster = base_path / "horus_heresy" / "hhv2.nightlords_zm.ros"


def post_files(multiple_pages, summary_page, use_icons):
    with test_roster.open() as roster_file:
        roster_file_text = roster_file.read()

    return client.post(
        "/files/",
        files={"file": roster_file_text},
        data={"multiple_pages": multiple_pages, "summary_page": summary_page, "use_icons": use_icons},
    )


def test__read_main():
    assert client.get("/").status_code == 200


def test__upload_roster():
    assert post_files(False, False, False).status_code == 200


def test__upload_roster_multipart_false():
    response = post_files(False, False, False)
    assert response.status_code == 200
    assert "single_page.css" in response.text


def test__upload_roster_multipart_true():
    assert post_files(True, False, False).status_code == 200
