from pathlib import Path
from unittest import TestCase

from starlette.testclient import TestClient

from src.main import app

client = TestClient(app)


class RenderingTests(TestCase):
    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters"
        self.zipped_roster = str(
            self.base_path / "zipped_rosters" / "elite_roster.rosz"
        )
        self.test_roster = str(
            self.base_path / "horus_heresy" / "legion_astartes_roster_new.ros"
        )

    def test__read_main(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test__upload_roster(self):
        multiple_pages = False
        summary_page = False
        with open(self.test_roster, "r") as roster_file:
            roster_file = roster_file.read()

        response = client.post(
            "/files/",
            files={"file": roster_file},
            data={"multiple_pages": multiple_pages, "summary_page": summary_page},
        )

        self.assertEqual(response.status_code, 200)

    def test__upload_roster_multipart_false(self):
        multiple_pages = False
        summary_page = False
        with open(self.test_roster, "r") as roster_file:
            roster_file = roster_file.read()

        response = client.post(
            "/files/",
            files={"file": roster_file},
            data={"multiple_pages": multiple_pages, "summary_page": summary_page},
        )
        multiple_pages_response = "single_page.css" in response.text

        self.assertEqual(response.status_code, 200)
        self.assertTrue(multiple_pages_response)

    def test__upload_roster_multipart_true(self):
        multiple_pages = True
        summary_page = False

        with open(self.test_roster, "r") as roster_file:
            roster_file = roster_file.read()

        response = client.post(
            "/files/",
            files={"file": roster_file},
            data={"multiple_pages": multiple_pages, "summary_page": summary_page},
        )

        multiple_pages_response = "multiple_pages.css" in response.text

        self.assertEqual(response.status_code, 200)
        self.assertTrue(multiple_pages_response)
