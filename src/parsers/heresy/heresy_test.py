from pathlib import Path

from src.models.heresy_unit import HeresyUnit
from src.parsers.heresy.heresy_constants import TOUGHNESS
from src.utils.test_utils import fetch_and_parse_roster

base_path = Path.cwd() / "test_rosters" / "horus_heresy"


def test__heresy_loop_through_test_folder_and_parse():
    """method: fetch_and_parse_roster(horus heresy)
    prerequisite: given an unzipped roster file it will parse without errors
    expected: successfully parses all roster files in the test folder.
    """
    parsed_rosters = []
    list_of_rosters = [file for file in base_path.iterdir() if file.is_file()]

    for roster in list_of_rosters:
        parsed_roster = fetch_and_parse_roster(roster_file=roster)
        parsed_rosters.append(parsed_roster)

    assert bool(parsed_rosters)


def test__stat_type_finder():
    """method: get_stat_type
    pre-req: should find the correct stat line for a unit
    expected: should return the toughness stat line.
    """
    test_unit_type = "infantry"
    stat_type = HeresyUnit.get_stat_type(test_unit_type)
    assert stat_type == TOUGHNESS.get("name")


def test_legion_zm_list():
    """
    Test a basic 1000 points night lords list
    contains and HQ with a command squad + a contemptor + several infantry units
    """
    hhv2_night_lords_zm = base_path / "hhv2.nightlords_zm.ros"
    parsed_roster = fetch_and_parse_roster(roster_file=hhv2_night_lords_zm)

    assert bool(parsed_roster) is True


def test_solar_aux_zm_list():
    """ """
    hhv2_solar_aux_zm = base_path / "hhv2.solar_aux_zm.ros"
    parsed_roster = fetch_and_parse_roster(roster_file=hhv2_solar_aux_zm)

    assert bool(parsed_roster) is True


def test_mechanicum_zm_list():
    """ """
    hhv2_mechanicum_zm = base_path / "hhv2.mechanicum_zm.ros"
    parsed_roster = fetch_and_parse_roster(roster_file=hhv2_mechanicum_zm)

    assert bool(parsed_roster) is True


def test_custodes_zm_list():
    """ """
    hhv2_custodes_zm = base_path / "hhv2.custodes_zm.ros"
    parsed_roster = fetch_and_parse_roster(roster_file=hhv2_custodes_zm)

    assert bool(parsed_roster) is True
