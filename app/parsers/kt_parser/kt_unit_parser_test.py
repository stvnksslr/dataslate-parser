from unittest import TestCase
from pathlib import Path

from app.parsers.kt_parser.kt_unit_parser import parse_units


class KTUnitParserTest(TestCase):

    def setUp(self):
        self.killteam_roster_path = Path.cwd() / "test_rosters" / "kill_team" / "chaos_roster.ros"

    def test_parse_units_test_for_killteam_returns_list(self):
        with open(self.killteam_roster_path, "r") as roster_file:
            contents = roster_file.read()
            parsed_roster = parse_units(contents=contents)
            self.assertTrue(parsed_roster)

    def test_parse_chaos_roster_for_killteam_returns_12_units(self):
        with open(self.killteam_roster_path, "r") as roster_file:
            contents = roster_file.read()
            parsed_roster = parse_units(contents=contents)
        self.assertEqual(len(parsed_roster), 12)

    def test_parse_chaos_roster_for_killteam_returns_properly_formatted_asp_champion(self):
        with open(self.killteam_roster_path, "r") as roster_file:
            contents = roster_file.read()
            parsed_roster = parse_units(contents=contents)

        aspiring_champion = parsed_roster[0]
        self.assertEqual(aspiring_champion.unit_name, "Aspiring Champion")
        self.assertEqual(aspiring_champion.movement, '6"')
        self.assertEqual(aspiring_champion.attacks, "2")
        self.assertEqual(aspiring_champion.ballistic_skill, "3+")
        self.assertEqual(aspiring_champion.weapon_skill, "3+")
        self.assertEqual(aspiring_champion.strength, '4')
        self.assertEqual(aspiring_champion.toughness, '4')
        self.assertEqual(aspiring_champion.wounds, '1')
        self.assertEqual(aspiring_champion.save, "3+")
        self.assertEqual(aspiring_champion.max, "1")
        self.assertEqual(len(aspiring_champion.keywords), 6)
        self.assertEqual(len(aspiring_champion.wargear), 5)
        self.assertTrue(aspiring_champion.wargear.get('Power fist'))
