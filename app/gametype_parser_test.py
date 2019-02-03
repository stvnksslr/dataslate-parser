from unittest import TestCase
from app import gametype_parser


class GameTypeParserTest(TestCase):
    def setUp(self):
        self.killteam = "killteam"
        self.game_type = "Warhammer 40,000: Kill Team (2018)"
        self.game_type_id = 'a467-5f42-d24c-6e5b'

    def test__find_game_type(self):
        """
        Method: find_game_type()
        Precondition: game_type killteam
        Result: list matches expected outcome
        """
        game_system = gametype_parser.find_game_type(self,
                                                     self.game_type,
                                                     self.game_type_id)

        self.assertEqual(game_system, self.killteam)
