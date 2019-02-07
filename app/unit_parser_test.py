from unittest import TestCase
from app.unit_parser import UnitParser


class UnitParserTest(TestCase):
    def setUp(self):
        self.unzipped_roster_path = "../test_rosters/unzipped/"
        self.killteam_roster_path = self.unzipped_roster_path + "test.ros"

    def test_parse_units_test_for_killteam(self):
        with open(self.killteam_roster_path, "r") as roster_file:
            contents = roster_file.read()
            parse_roster = UnitParser.parse_units(contents=contents)
            self.assertTrue(parse_roster)
