from pathlib import Path
from unittest import TestCase

from app.tests.test_utils import fetch_and_parse_roster


class HeresyTest(TestCase):

    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters" / "horus_heresy"
        self.night_lords_zm_force = str(self.base_path / "test_hh.ros")
        self.gametype = "heresy"

    def test__parse_heresy_roster_without_errors(self):
        parsed_roster = fetch_and_parse_roster(roster_file=self.night_lords_zm_force, gametype=self.gametype)
        self.assertTrue(parsed_roster)

    def test__parses_three_units_from_roster(self):
        parsed_roster = fetch_and_parse_roster(roster_file=self.night_lords_zm_force, gametype=self.gametype)
        self.assertEqual(len(parsed_roster), 3)

    def test__legion_tactical_squad_has_sarge_and_unit(self):
        parsed_roster = fetch_and_parse_roster(roster_file=self.night_lords_zm_force, gametype=self.gametype)
        self.assertEqual(len(parsed_roster), 3)

        self.assertEqual(parsed_roster[0].list_of_units[0].name, 'Legion Tactical Space Marine')
        self.assertEqual(parsed_roster[0].list_of_units[1].name, 'Legion Tactical Sergeant')

    def test__praetor_correctly_parsed(self):
        parsed_roster = fetch_and_parse_roster(roster_file=self.night_lords_zm_force, gametype=self.gametype)
        self.assertTrue(parsed_roster[1].list_of_units[0])
        self.assertEqual(len(parsed_roster[1].list_of_units), 1)

        self.assertEqual(parsed_roster[1].list_of_units[0].name, 'Legion Praetor')
        self.assertEqual(parsed_roster[1].list_of_units[0].unit_type, 'Infantry (Character)')

    def test__terror_squad_correctly_parsed(self):
        parsed_roster = fetch_and_parse_roster(roster_file=self.night_lords_zm_force, gametype=self.gametype)
        self.assertEqual(len(parsed_roster[2].list_of_units), 2)

        self.assertEqual(parsed_roster[2].list_of_units[0].name, 'Executioner')
        self.assertEqual(parsed_roster[2].list_of_units[0].unit_type, 'Infantry')

        self.assertEqual(parsed_roster[2].list_of_units[1].name, 'Headsman')
        self.assertEqual(parsed_roster[2].list_of_units[1].unit_type, 'Infantry')
