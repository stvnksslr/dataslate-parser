from pathlib import Path
from unittest import TestCase

from starlette.testclient import TestClient

from app.utils.test_utils import fetch_and_parse_roster
from main import app

client = TestClient(app)


class RenderingTests(TestCase):
    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters" / "horus_heresy"
        self.chaos_kill_team_standard = str(
            self.base_path / "parser_test_full_list.ros"
        )
        self.gametype = "heresy"

        self.test_roster = str(self.base_path / "legion_astartes_roster_new.ros")

        self.parsed_roster = fetch_and_parse_roster(
            roster_file=self.chaos_kill_team_standard, gametype=self.gametype
        )

    def test_read_main(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"msg": "Hello World"})

    # def test_render_killteam_via_context(self):
    #     response = client.get("/render/sandbox")
    #     self.assertEqual(response.status_code, 200)

    def test_upload_roster(self):
        with open(self.test_roster, "r") as roster_file:
            contents = roster_file.read()

        response = client.post("/files/", files=dict(file=contents))

        self.assertEqual(response.status_code, 200)
