from os import listdir
from os.path import isfile, join
from pathlib import Path

from src.models.heresy_unit import HeresyUnit
from src.parsers.heresy.heresy_constants import TOUGHNESS
from src.parsers.heresy.rules_summary import get_rules_summary
from src.utils.test_utils import fetch_and_parse_roster

base_path = Path.cwd() / "test_rosters" / "horus_heresy"
new_bs_format = str(base_path / "legion_astartes_roster_new.ros")
full_list = str(base_path / "parser_test_full_list.ros")
tac_squad_with_dt = str(base_path / "tac_squad_with_dt.ros")
list_with_wargear = str(base_path / "wargear_fix.ros")
porch_slam = str(base_path / "porch_slam_saux.ros")
legion_list_8_19_20 = str(base_path / "updated_legions_roster_8_19-20.ros")
legion_list_9_5_21 = str(base_path / "2021_9_5_test_roster.ros")


def test__heresy_loop_through_test_folder_and_parse():
    """
    method: fetch_and_parse_roster(horus heresy)
    prerequisite: given a unzipped roster file it will parse without errors
    expected: successfully parses all roster files in the test folder
    """
    parsed_rosters = []
    list_of_rosters = [file for file in listdir(str(base_path)) if isfile(join(str(base_path), file))]

    for roster in list_of_rosters:
        parsed_roster = fetch_and_parse_roster(roster_file=str(base_path) + "/" + roster)
        parsed_rosters.append(parsed_roster)

    assert bool(parsed_rosters) == True


def test__new_bs_format():
    """
    method: fetch_and_parse_roster(heresy)
    prerequisite: given a 2.02+ format roster
    expected: successfully parses all three entries in the roster
    """
    parsed_roster = fetch_and_parse_roster(roster_file=new_bs_format)
    assert bool(parsed_roster) == True
    assert len(parsed_roster) == 3


def test__full_list():
    """
    method: fetch_and_parse_roster(killteam)
    prerequisite: given a 2.02+ format roster that contains infantry, vehicles, fliers
    expected: successfully parses all 12 entries in the roster
    """
    parsed_roster = fetch_and_parse_roster(roster_file=full_list)

    assert bool(parsed_roster)
    assert len(parsed_roster) == 12


def test__tac_squad_with_dt():
    """
    method: fetch_and_parse_roster(heresy)
    prerequisite: given a 2.02+ format roster that contains an infantry unit
    with a dedicated transport
    expected: successfully parses both the infantry unit and the dedicated transport
    """
    parsed_roster = fetch_and_parse_roster(roster_file=tac_squad_with_dt)

    assert bool(parsed_roster) == True
    assert len(parsed_roster[0].list_of_units) == 3
    assert parsed_roster[0].list_of_units[0].name == "legion tactical space marine"
    assert parsed_roster[0].list_of_units[1].name == "legion tactical sergeant"
    assert parsed_roster[0].list_of_units[2].name == "legion rhino"


def test__tac_squad_with_dt_characteristics():
    """
    method: fetch_and_parse_roster(heresy)
    prerequisite: given a 2.02+ format roster that contains an infantry unit
    with a dedicated transport
    expected: successfully parses both the infantry unit and the dedicated transport
    """
    parsed_roster = fetch_and_parse_roster(roster_file=tac_squad_with_dt)
    tactical_squad = parsed_roster[0].list_of_units

    assert bool(parsed_roster) == True
    assert parsed_roster[0].list_of_units[0].name == "legion tactical space marine"
    assert tactical_squad[0].attacks == "1"
    assert tactical_squad[0].ballistic_skill == "4"
    assert tactical_squad[0].initiative == "4"
    assert tactical_squad[0].leadership == "8"
    assert tactical_squad[0].save == "3+"
    assert tactical_squad[0].strength == "4"
    assert tactical_squad[0].toughness == "4"
    assert tactical_squad[0].unit_type == "infantry"
    assert tactical_squad[0].weapon_skill == "4"
    assert tactical_squad[0].wounds == "1"


def test__stat_type_finder():
    """
    method: get_stat_type
    pre-req: should find the correct stat line for a unit
    expected: should return the toughness stat line
    """
    test_unit_type = "infantry"
    stat_type = HeresyUnit.get_stat_type(test_unit_type)
    assert stat_type == TOUGHNESS.get("name")


def test_wargear_additions():
    """
    method: fetch_and_parse_roster
    pre-req: should take in an input and find the correct wargear for this specific unit
    expected: should return 2 pieces of wargear
    """
    parsed_roster = fetch_and_parse_roster(roster_file=list_with_wargear)
    unit_with_wargear = parsed_roster[0].list_of_units[0]
    assert bool(parsed_roster) == True
    assert len(unit_with_wargear.wargear) == 2


def test_weapon_additions():
    """
    method: fetch_and_parse_roster
    pre-req: should take in an input and find the correct weapons for this specific unit
    expected: should return two weapons
    """
    parsed_roster = fetch_and_parse_roster(roster_file=list_with_wargear)
    unit_with_weapon = parsed_roster[0].list_of_units[0]

    assert bool(parsed_roster) == True
    assert len(unit_with_weapon.weapon) == 2


def test_rules_summary():
    """
    method: get_rules_summary()
    pre-req: take a parsed list and create a dict of rules no duplicates
    expected: should return all the rules from the input list
    """
    parsed_roster = fetch_and_parse_roster(roster_file=list_with_wargear)
    rules_summary = get_rules_summary(parsed_roster)
    assert len(rules_summary) == 16


def test_legion_list_8_19_20():
    """
    method: get_rules_summary()
    pre-req: take a parsed list and create a dict of rules no duplicates
    expected: new mounrival and super heavy categories should parse correctly and not break the parse
    """
    parsed_roster = fetch_and_parse_roster(roster_file=legion_list_8_19_20)
    assert len(parsed_roster) == 3


def test_legion_list_5_5_2021():
    """
    method: get_rules_summary()
    pre-req: take a parsed list and create a dict of rules no duplicates
    expected: new mounrival and super heavy categories should parse correctly and not break the parse
    """
    parsed_roster = fetch_and_parse_roster(roster_file=legion_list_9_5_21)
    assert len(parsed_roster) == 3
