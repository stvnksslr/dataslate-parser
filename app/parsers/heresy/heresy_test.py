from os import listdir
from os.path import isfile, join
from pathlib import Path
from unittest import TestCase

from app.utils.test_utils import fetch_and_parse_roster


class HeresyTest(TestCase):
    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters" / "horus_heresy"
        self.new_bs_format = str(self.base_path / "legion_astartes_roster_new.ros")
        self.full_list = str(self.base_path / "parser_test_full_list.ros")
        self.tac_squad_with_dt = str(self.base_path / "tac_squad_with_dt.ros")

    def test__loop_through_test_folder_and_parse(self):
        """
        method: fetch_and_parse_roster(horus heresy)
        prerequisite: given a unzipped roster file it will parse without errors
        expected: successfully parses all roster files in the test folder
        """
        parsed_rosters = []
        list_of_rosters = [
            file
            for file in listdir(str(self.base_path))
            if isfile(join(str(self.base_path), file))
        ]

        for roster in list_of_rosters:
            parsed_roster = fetch_and_parse_roster(
                roster_file=str(self.base_path) + "/" + roster
            )
            parsed_rosters.append(parsed_roster)

        self.assertTrue(parsed_rosters)

    def test__new_bs_format(self):
        """
        method: fetch_and_parse_roster(heresy)
        prerequisite: given a 2.02+ format roster
        expected: successfully parses all three entries in the roster
        """
        parsed_roster = fetch_and_parse_roster(roster_file=self.new_bs_format)
        self.assertTrue(parsed_roster)
        self.assertTrue(len(parsed_roster), 3)

    def test__full_list(self):
        """
        method: fetch_and_parse_roster(killteam)
        prerequisite: given a 2.02+ format roster that contains infantry, vehicles, fliers
        expected: successfully parses all 12 entries in the roster
        """
        parsed_roster = fetch_and_parse_roster(roster_file=self.full_list)

        self.assertTrue(parsed_roster)
        self.assertEqual(len(parsed_roster), 12)

    def test__tac_squad_with_dt(self):
        """
        method: fetch_and_parse_roster(heresy)
        prerequisite: given a 2.02+ format roster that contains an infantry unit
        with a dedicated transport
        expected: successfully parses both the infantry unit and the dedicated transport
        """
        parsed_roster = fetch_and_parse_roster(roster_file=self.tac_squad_with_dt)

        self.assertTrue(parsed_roster)
        self.assertEqual(len(parsed_roster[0].list_of_units), 3)
        self.assertEqual(
            parsed_roster[0].list_of_units[0].name, "legion tactical space marine"
        )
        self.assertEqual(
            parsed_roster[0].list_of_units[1].name, "legion tactical sergeant"
        )
        self.assertEqual(parsed_roster[0].list_of_units[2].name, "legion rhino")

    def test__tac_squad_with_dt_characteristics(self):
        """
        method: fetch_and_parse_roster(heresy)
        prerequisite: given a 2.02+ format roster that contains an infantry unit
        with a dedicated transport
        expected: successfully parses both the infantry unit and the dedicated transport
        """
        parsed_roster = fetch_and_parse_roster(roster_file=self.tac_squad_with_dt)
        tactical_squad = parsed_roster[0].list_of_units
        self.assertTrue(parsed_roster)
        self.assertEqual(
            parsed_roster[0].list_of_units[0].name, "legion tactical space marine"
        )
        self.assertEqual(tactical_squad[0].attacks, "1")
        self.assertEqual(tactical_squad[0].ballistic_skill, "4")
        self.assertEqual(tactical_squad[0].initiative, "4")
        self.assertEqual(tactical_squad[0].leadership, "8")
        self.assertEqual(tactical_squad[0].movement, 6)
        self.assertEqual(tactical_squad[0].save, "3+")
        self.assertEqual(tactical_squad[0].strength, "4")
        self.assertEqual(tactical_squad[0].toughness, "4")
        self.assertEqual(tactical_squad[0].unit_type, "infantry")
        self.assertEqual(tactical_squad[0].weapon_skill, "4")
        self.assertEqual(tactical_squad[0].wounds, "1")
