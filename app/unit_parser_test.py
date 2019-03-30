from unittest import TestCase
from app.unit_parser import UnitParser
from pathlib import Path


class UnitParserTest(TestCase):

    def setUp(self):
        self.killteam_roster_path = Path.cwd() / "test_rosters" / "unzipped" / "test.ros"

    def test_parse_units_test_for_killteam(self):
        with open(self.killteam_roster_path, "r") as roster_file:
            contents = roster_file.read()
            parse_roster = UnitParser.parse_units(contents=contents)
            self.assertTrue(parse_roster)
