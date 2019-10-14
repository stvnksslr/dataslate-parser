from pathlib import Path
from unittest import TestCase

from app.parsers.gametype.gametype import detect_gametype, find_gametype_parser
from app.parsers.heresy import heresy
from app.utils.constants import HORUS_HERESY_ID


class GametypeTest(TestCase):
    def setUp(self):
        self.base_path = Path.cwd() / "test_rosters" / "horus_heresy"

        self.heresy_roster = str(self.base_path / "legion_astartes_roster_new.ros")
        self.killteam_roster = "killteam"

    def test__detect_gametype(self):
        with open(self.heresy_roster, "r") as roster_file:
            contents = roster_file.read()

        gametype = detect_gametype(roster=contents)

        self.assertEqual(gametype, HORUS_HERESY_ID)

    def test__return_parser(self):
        with open(self.heresy_roster, "r") as roster_file:
            contents = roster_file.read()

        gametype = detect_gametype(roster=contents)

        parser = find_gametype_parser(gametype)

        self.assertEqual(parser, heresy)
