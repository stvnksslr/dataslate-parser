from pathlib import Path
from unittest import TestCase

from starlette.testclient import TestClient

from app.tests.test_utils import fetch_and_parse_roster
from main import app

client = TestClient(app)


class RenderingTests(TestCase):
    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters" / "kill_team"
        self.chaos_kill_team_standard = str(
            self.base_path / "test_roster_chaos_new.ros"
        )
        self.gametype = "killteam"

    def test_read_main(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"msg": "Hello World"})

    # def test_basic_kill_team_roster(self):
    #     parsed_roster = fetch_and_parse_roster(
    #         roster_file=self.chaos_kill_team_standard, gametype=self.gametype
    #     )
    #     response = client.get("render/kt/roster")
    #     assert response.status_code == 200
