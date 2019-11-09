from pathlib import Path
from unittest import TestCase

from starlette.testclient import TestClient

from app.main import app

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

    def test_read_main(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_upload_roster(self):
        with open(self.test_roster, "r") as roster_file:
            contents = roster_file.read()

        response = client.post("/files/", files=dict(file=contents))

        self.assertEqual(response.status_code, 200)
