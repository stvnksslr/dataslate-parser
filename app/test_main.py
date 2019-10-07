from pathlib import Path
from unittest import TestCase

from starlette.requests import Request
from starlette.testclient import TestClient

from app.utils.test_utils import fetch_and_parse_roster
from main import app, templates

client = TestClient(app)


class RenderingTests(TestCase):
    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters" / "kill_team"
        self.chaos_kill_team_standard = str(
            self.base_path / "test_roster_chaos_new.ros"
        )
        self.gametype = "killteam"

        self.parsed_roster = fetch_and_parse_roster(
            roster_file=self.chaos_kill_team_standard, gametype=self.gametype
        )

    def test_read_main(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"msg": "Hello World"})

    def test_render_killteam_via_context(self):
        response = client.get("/render/sandbox")
        self.assertEqual(response.status_code, 200)
