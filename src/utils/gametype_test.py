from pathlib import Path
from unittest import TestCase

from src.utils.battlescribe_meta import check_battlescribe_version
from src.utils.gametype import detect_gametype, find_gametype_parser
from src.parsers.heresy import heresy
from src.utils.constants import HORUS_HERESY_ID


class GametypeTest(TestCase):
    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters" / "horus_heresy"

        self.heresy_roster = str(self.base_path / "legion_astartes_roster_new.ros")
        self.killteam_roster = "killteam"

    def test__detect_gametype(self):
        with open(self.heresy_roster, "r") as roster_file:
            roster_file = roster_file.read()

        gametype = detect_gametype(roster=roster_file)

        self.assertEqual(gametype, HORUS_HERESY_ID)

    def test__return_parser(self):
        with open(self.heresy_roster, "r") as roster_file:
            roster_file = roster_file.read()

        gametype = detect_gametype(roster=roster_file)

        parser = find_gametype_parser(gametype)

        self.assertEqual(parser, heresy)

    def test__check_battlescribe_version(self):
        with open(self.heresy_roster, "r") as roster_file:
            roster_file = roster_file.read()

        supported_version = check_battlescribe_version(roster=roster_file)
        self.assertTrue(supported_version)
