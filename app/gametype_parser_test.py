from unittest import TestCase
from lib import gametype_parser


class GameTypeParserTest(TestCase):
    def setUp(self):
        self.killteam = "killteam"
        self.gameSystemName = "Warhammer 40,000: Kill Team (2018)"

    def test__find_game_type(self):
        """
        Method: find_gametype()
        Precondition: gametype killteam
        Result: list matches expected outcome
        """
        gamesystem = gametype_parser.GameTypeParser.find_gametype(
            self, self.gameSystemName
        )
        self.assertEqual(gamesystem, self.killteam)
