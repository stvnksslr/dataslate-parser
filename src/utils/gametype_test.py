from pathlib import Path

from src.utils.battlescribe_meta import check_battlescribe_version
from src.utils.gametype import detect_gametype, find_gametype_parser
from src.parsers.heresy import heresy
from src.utils.constants import HORUS_HERESY_ID

base_path = Path.cwd() / "test_rosters" / "horus_heresy"
heresy_roster = str(base_path / "legion_astartes_roster_new.ros")
killteam_roster = "killteam"


def test__detect_gametype():
    with open(heresy_roster, "r") as roster_file:
        roster_file = roster_file.read()

    gametype = detect_gametype(roster=roster_file)

    assert gametype == HORUS_HERESY_ID


def test__return_parser():
    with open(heresy_roster, "r") as roster_file:
        roster_file = roster_file.read()

    gametype = detect_gametype(roster=roster_file)

    parser = find_gametype_parser(gametype)

    assert parser == heresy


def test__check_battlescribe_version():
    with open(heresy_roster, "r") as roster_file:
        roster_file = roster_file.read()

    supported_version = check_battlescribe_version(roster=roster_file)
    assert supported_version
