from unittest import TestCase
from pathlib import Path

from app.parsers.kt_parser.kt_parser import parse_units


class KTUnitParserTest(TestCase):

    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters" / "kill_team"
        self.chaos_kill_team_standard = str(self.base_path / "chaos_roster.ros")
        self.death_guard_kill_team_with_commander = str(self.base_path / "death_guard_test_with_commander.ros")
        self.ability_example_name = "Death to the False Emperor"

    def test__parse_units_test_for_killteam_returns_list(self):
        with open(self.chaos_kill_team_standard, "r") as roster_file:
            contents = roster_file.read()
            parsed_roster = parse_units(contents=contents)
            self.assertTrue(parsed_roster)

    def test__parse_chaos_roster_for_killteam_returns_12_units(self):
        with open(self.chaos_kill_team_standard, "r") as roster_file:
            contents = roster_file.read()
            parsed_roster = parse_units(contents=contents)
        self.assertEqual(len(parsed_roster), 12)

    def test__parse_chaos_roster_for_killteam_returns_properly_formatted_asp_champion(self):
        with open(self.chaos_kill_team_standard, "r") as roster_file:
            contents = roster_file.read()
            parsed_roster = parse_units(contents=contents)

        aspiring_champion = parsed_roster[0]
        self.assertEqual(aspiring_champion.name, "Aspiring Champion")
        self.assertEqual(aspiring_champion.movement, '6"')
        self.assertEqual(aspiring_champion.attacks, "2")
        self.assertEqual(aspiring_champion.ballistic_skill, "3+")
        self.assertEqual(aspiring_champion.weapon_skill, "3+")
        self.assertEqual(aspiring_champion.strength, '4')
        self.assertEqual(aspiring_champion.toughness, '4')
        self.assertEqual(aspiring_champion.wounds, '1')
        self.assertEqual(aspiring_champion.save, "3+")
        self.assertEqual(aspiring_champion.max, "1")
        self.assertEqual(aspiring_champion.leadership, "8")
        self.assertEqual(len(aspiring_champion.keywords), 6)
        self.assertEqual(len(aspiring_champion.wargear), 5)
        self.assertTrue(aspiring_champion.wargear.get('Power fist'))
        self.assertEqual(len(aspiring_champion.abilities), 3)
        self.assertTrue(aspiring_champion.abilities.get(self.ability_example_name))

    def test__parse_death_guard_roster_with_commander(self):
        with open(self.death_guard_kill_team_with_commander, "r") as roster_file:
            contents = roster_file.read()
            parsed_roster = parse_units(contents=contents)

        plague_surgeon_commander = parsed_roster[0]
        self.assertTrue(len(parsed_roster), 8)
        self.assertTrue(len(plague_surgeon_commander.abilities), 11)
        self.assertTrue(len(plague_surgeon_commander.keywords), 8)
        self.assertTrue(len(plague_surgeon_commander.wargear), 4)
        self.assertTrue(plague_surgeon_commander.wounds, 4)
        self.assertTrue(plague_surgeon_commander.wargear.get('Balesword'))
