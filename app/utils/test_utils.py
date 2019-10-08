from pathlib import Path

from app.utils.constants import SUPPORTED_PARSERS


def fetch_and_parse_roster(roster_file, gametype):
    with open(roster_file, "r") as roster_file:
        contents = roster_file.read()
        parser = get_parser_method(gametype)
        parsed_roster = parser.parse_units(contents=contents)
        return parsed_roster


def get_parser_method(gametype):
    parser = None
    try:
        parser = SUPPORTED_PARSERS.get(gametype)
    except Exception:
        print("Parser not supported")
    return parser


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
