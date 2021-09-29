from os import listdir
from os.path import isfile, join
from pathlib import Path

from src.utils.test_utils import fetch_and_parse_roster

base_path = Path.cwd() / "test_rosters" / "kill_team"
gametype = "killteam"


def test__killteam_loop_through_test_folder_and_parse():
    """
    method: fetch_and_parse_roster(killteam)
    prerequisite: given a unzipped roster file it will parse without errors
    expected: successfully parses all roster files in the test folder
    """
    parsed_rosters = []
    list_of_rosters = [file for file in listdir(str(base_path)) if isfile(join(str(base_path), file))]

    for roster in list_of_rosters:
        parsed_roster = fetch_and_parse_roster(roster_file=str(base_path) + "/" + roster)
        parsed_rosters.append(parsed_roster)

    assert bool(parsed_rosters)


def test__killteam_parse_chaos_killteam():
    chaos_killteam_path = str(base_path / "chaos_killteam.ros")
    parsed_roster = fetch_and_parse_roster(roster_file=chaos_killteam_path)

    assert bool(parsed_roster)
    assert len(parsed_roster) == 11
    assert parsed_roster[0].name == "Aspiring Champion"
    assert len(parsed_roster[0].wargear) == 3


def test__killteam_parse_vet_guardsman_killteam():
    vet_guardsmen_path = str(base_path / "vet_guard.ros")
    parsed_roster = fetch_and_parse_roster(roster_file=vet_guardsmen_path)

    assert bool(parsed_roster)
    assert len(parsed_roster) == 10
    assert parsed_roster[0].name == "Gunner Veteran"
    assert len(parsed_roster[0].wargear) == 3
