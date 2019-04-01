from unittest import TestCase
from app.unit_parser import UnitParser
from pathlib import Path


class UnitParserTest(TestCase):

    def setUp(self):
        self.killteam_roster_path = Path.cwd() / "test_rosters" / "unzipped" / "test.ros"

    def test_parse_units_test_for_killteam_returns_list(self):
        with open(self.killteam_roster_path, "r") as roster_file:
            contents = roster_file.read()
            parsed_roster = UnitParser.parse_units(contents=contents)
            self.assertTrue(parsed_roster)

    def test_parse_chaos_roster_for_killteam_returns_12_units(self):
        with open(self.killteam_roster_path, "r") as roster_file:
            contents = roster_file.read()
            parsed_roster = UnitParser.parse_units(contents=contents)
        self.assertEqual(len(parsed_roster), 12)

    def test_parse_chaos_roster_for_killteam_returns_properly_formatted_asp_champion(self):
        with open(self.killteam_roster_path, "r") as roster_file:
            contents = roster_file.read()
            parsed_roster = UnitParser.parse_units(contents=contents)
        asp_champ = parsed_roster[0]
        self.assertEqual(asp_champ.unit_name, "Aspiring Champion")
        self.assertEqual(asp_champ.movement, '6"')
        self.assertEqual(asp_champ.attacks, "2")
        self.assertEqual(asp_champ.ballistic_skill, "3+")
        self.assertEqual(asp_champ.weapon_skill, "3+")
        self.assertEqual(asp_champ.strength, '4')
        self.assertEqual(asp_champ.toughness, '4')
        self.assertEqual(asp_champ.wounds, '1')
        self.assertEqual(asp_champ.save, "3+")
        self.assertEqual(asp_champ.max, "1")
        self.assertEqual(len(asp_champ.keywords), 6)
