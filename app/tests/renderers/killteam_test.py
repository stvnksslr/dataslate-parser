from pathlib import Path
from unittest import TestCase

from app.renderers.killteam import render_roster
from app.tests.test_utils import fetch_and_parse_roster


class KillteamTest(TestCase):

    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters" / "kill_team"
        self.chaos_kill_team_standard = str(self.base_path / "chaos_roster.ros")
        self.gametype = "killteam"

    def test__render_parsed_roster(self):
        parsed_roster = fetch_and_parse_roster(
            roster_file=self.chaos_kill_team_standard, gametype=self.gametype)
        roster_image = render_roster(parsed_roster)
        self.assertTrue(roster_image)
