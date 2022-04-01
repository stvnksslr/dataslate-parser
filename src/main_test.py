from pathlib import Path

from starlette.testclient import TestClient

from src.main import app

client = TestClient(app)


base_path = Path.cwd() / "test_rosters"
zipped_roster = str(base_path / "zipped_rosters" / "elite_roster.rosz")
test_roster = str(base_path / "horus_heresy" / "legion_astartes_roster_new.ros")


def test__read_main():
    response = client.get("/")
    assert response.status_code == 200


def test__upload_roster():
    multiple_pages = False
    summary_page = False
    use_icons = False
    with open(test_roster, "r") as roster_file:
        roster_file = roster_file.read()

    response = client.post(
        "/files/",
        files={"file": roster_file},
        data={"multiple_pages": multiple_pages, "summary_page": summary_page, "use_icons": use_icons},
    )

    assert response.status_code == 200


def test__upload_roster_multipart_false():
    multiple_pages = False
    summary_page = False
    use_icons = False
    with open(test_roster, "r") as roster_file:
        roster_file = roster_file.read()

    response = client.post(
        "/files/",
        files={"file": roster_file},
        data={"multiple_pages": multiple_pages, "summary_page": summary_page, "use_icons": use_icons},
    )
    multiple_pages_response = "single_page.css" in response.text

    assert response.status_code == 200
    assert multiple_pages_response


def test__upload_roster_multipart_true():
    multiple_pages = True
    summary_page = False
    use_icons = False

    with open(test_roster, "r") as roster_file:
        roster_file = roster_file.read()

    response = client.post(
        "/files/",
        files={"file": roster_file},
        data={"multiple_pages": multiple_pages, "summary_page": summary_page, "use_icons": use_icons},
    )

    multiple_pages_response = "multiple_pages.css" in response.text

    assert response.status_code == 200
    assert multiple_pages_response
