from pathlib import Path

from app.parsers.gametype.gametype import (
    detect_gametype,
    find_gametype_parser,
    find_template,
)
from app.utils.constants import SUPPORTED_PARSERS


def fetch_and_parse_roster(roster_file, gametype):
    with open(roster_file, "r") as roster_file:
        contents = roster_file.read()
        gametype = detect_gametype(contents)
        parser = find_gametype_parser(gametype)
        parsed_roster = parser.parse_units(contents=contents)
        return parsed_roster


def get_parser_and_parse_roster(roster):
    gametype = detect_gametype(roster)
    parser = find_gametype_parser(gametype)
    template = find_template(gametype)

    parsed_roster = parser.parse_units(contents=roster)
    return {"roster": parsed_roster, "template": template}


def generate_test_roster_heresy():
    base_path = Path.cwd() / "test_rosters" / "horus_heresy"
    chaos_kill_team_standard = str(base_path / "parser_test_full_list.ros")
    gametype = "heresy"
    parsed_roster = fetch_and_parse_roster(
        roster_file=chaos_kill_team_standard, gametype=gametype
    )
    return parsed_roster


def generate_test_roster():
    base_path = Path.cwd() / "test_rosters" / "kill_team"
    chaos_kill_team_standard = str(base_path / "test_roster_commander.ros")
    gametype = "killteam"
    parsed_roster = fetch_and_parse_roster(
        roster_file=chaos_kill_team_standard, gametype=gametype
    )
    return parsed_roster
