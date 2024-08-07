from os import listdir
from pathlib import Path

from src.utils.test_utils import fetch_and_parse_roster, fetch_and_parse_rules

base_path = Path.cwd() / "test_rosters" / "w40k"
gametype = "w40k"


def test__w40k_loop_through_test_folder_and_parse():
    """method: fetch_and_parse_roster(w40k)
    prerequisite: given a unzipped roster file it will parse without errors
    expected: successfully parses all roster files in the test folder.
    """
    parsed_rosters = []
    list_of_rosters = [file for file in listdir(base_path) if Path.is_file(base_path / file)]

    for roster in list_of_rosters:
        parsed_roster = fetch_and_parse_roster(roster_file=base_path / roster)
        parsed_rosters.append(parsed_roster)

    assert bool(parsed_rosters)


def test__w40k_parse_ultramar_test1():
    """method: fetch_and_parse_roster(w40k)
    prerequisite: given a unzipped roster file it will parse without errors
    expected: successfully parses all roster files in the test folder.
    """
    ultramar_test1_path = base_path / "ultramar_test1.ros"
    parsed_roster = fetch_and_parse_roster(roster_file=ultramar_test1_path)

    assert bool(parsed_roster)
    assert len(parsed_roster) == 4
    assert parsed_roster[0].name == "Intercessor Squad"
    assert len(parsed_roster[0].wargear) == 4


def test__w40k_parse_ultramar_test2():
    """method: fetch_and_parse_roster(w40k)
    prerequisite: given a unzipped roster file it will parse without errors
    expected: successfully parses all roster files in the test folder.
    """
    ultramar_test2_path = base_path / "ultramar_test2.ros"
    parsed_roster = fetch_and_parse_roster(roster_file=ultramar_test2_path)

    assert bool(parsed_roster)
    assert len(parsed_roster) == 5
    assert parsed_roster[0].name == "Hellblaster Squad"
    assert len(parsed_roster[0].wargear) == 5


def test_rules_summary():
    """method: fetch_and_parse_rules()
    pre-req: take a parsed list and create a dict of rules no duplicates
    expected: should return all the rules from the input list.
    """
    ultramar_test2_path = base_path / "ultramar_test2.ros"
    rules_summary = fetch_and_parse_rules(roster_file=ultramar_test2_path)
    assert len(rules_summary) == 7
