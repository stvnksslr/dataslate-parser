from pathlib import Path
from unittest import TestCase

from app.parsers.test_utils import fetch_and_parse_roster


class HeresyTest(TestCase):

    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters" / "horus_heresy"
        self.night_lords_zm_force = str(self.base_path / "test_hh.ros")
        self.gametype = "heresy"

    def test__parse_heresy_roster_without_errors(self):
        parsed_roster = fetch_and_parse_roster(roster_file=self.night_lords_zm_force, gametype=self.gametype)
        self.assertTrue(parsed_roster)
