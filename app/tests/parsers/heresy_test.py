from os import listdir
from os.path import isfile, join
from pathlib import Path
from unittest import TestCase

from app.tests.test_utils import fetch_and_parse_roster


class HeresyTest(TestCase):
    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters" / "horus_heresy"
        self.new_bs_format = str(self.base_path / "legion_astartes_roster_new.ros")
        self.gametype = "heresy"

    def test__loop_through_test_folder_and_parse(self):
        """
        method: fetch_and_parse_roster(killteam)
        prerequisite: given a unzipped roster file it will parse without errors
        expected: successfully parses all roster files in the test folder
        """
        parsed_rosters = []
        list_of_rosters = [
            f for f in listdir(str(self.base_path))
            if isfile(join(str(self.base_path), f))]

        for roster in list_of_rosters:
            parsed_roster = fetch_and_parse_roster(
                roster_file=str(self.base_path) + "/" + roster, gametype=self.gametype
            )
            parsed_rosters.append(parsed_roster)

        self.assertTrue(parsed_rosters)

    def test__new_bs_format(self):
        parsed_roster = fetch_and_parse_roster(
            roster_file=self.new_bs_format, gametype=self.gametype)

        self.assertTrue(parsed_roster)
