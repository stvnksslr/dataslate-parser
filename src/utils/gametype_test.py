from pathlib import Path

from src.parsers.heresy import heresy
from src.utils.battlescribe_meta import check_battlescribe_version
from src.utils.constants import HORUS_HERESY_ID
from src.utils.gametype import detect_gametype, find_gametype_parser

base_path = Path.cwd() / "test_rosters" / "horus_heresy"
heresy_roster = str(base_path / "legion_astartes_roster_new.ros")
killteam_roster = "killteam"


def test__detect_gametype():
    with Path.open(heresy_roster) as roster_file:
        roster_file_contents = roster_file.read()

    gametype = detect_gametype(roster=roster_file_contents)

    assert gametype == HORUS_HERESY_ID


def test__return_parser():
    with Path.open(heresy_roster) as roster_file:
        roster_file_contents = roster_file.read()

    gametype = detect_gametype(roster=roster_file_contents)

    parser = find_gametype_parser(gametype)

    assert parser == heresy


def test__check_battlescribe_version():
    with Path.open(heresy_roster) as roster_file:
        roster_file_contents = roster_file.read()

    supported_version = check_battlescribe_version(roster=roster_file_contents)
    assert supported_version
