from unittest import TestCase

from app.constants import KILLTEAM_ID, KILLTEAM_NAME
from app.game_type_parser import find_game_type


class GameTypeParser(TestCase):
    def setUp(self):
        self.game_type_id = KILLTEAM_ID
        self.game_type_name = KILLTEAM_NAME

    def test_find_game_type_test(self):
        found_game = find_game_type(self.game_type_id)
        self.assertTrue(found_game)
