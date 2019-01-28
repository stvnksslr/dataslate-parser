from unittest import TestCase
from app import gametype_parser


class GameTypeParserTest(TestCase):
    def setUp(self):
        self.killteam = "killteam"
        self.gameSystemName = "Warhammer 40,000: Kill Team (2018)"
        self.gameSystemId = 'a467-5f42-d24c-6e5b'

    def test__find_game_type(self):
        """
        Method: find_gametype()
        Precondition: gametype killteam
        Result: list matches expected outcome
        """
        gamesystem = gametype_parser.find_gametype(
            self, self.gameSystemName, self.gameSystemId
        )
        self.assertEqual(gamesystem, self.killteam)
