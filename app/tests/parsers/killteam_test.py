from unittest import TestCase
from pathlib import Path
from app.tests.test_utils import fetch_and_parse_roster
from os import listdir
from os.path import isfile, join


class KillteamTest(TestCase):
    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters" / "kill_team"
        self.chaos_kill_team_standard = str(self.base_path / "chaos_roster.ros")
        self.death_guard_kill_team_with_commander = str(
            self.base_path / "death_guard_with_commander.ros"
        )
        self.ability_example_name = "Death to the False Emperor"
        self.gametype = "killteam"
        self.new_bs_format = str(self.base_path / "test_roster_chaos_new.ros")

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
            roster_file=self.new_bs_format, gametype=self.gametype
        )
        self.assertTrue(parsed_roster)
