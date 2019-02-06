from unittest import TestCase

from app.constants import KILLTEAM_ID, KILLTEAM_NAME
from app.game_type_parser import find_game_type


class GameTypeParser(TestCase):
    def setUp(self):
        self.game_type_id = KILLTEAM_ID
        self.game_type_name = KILLTEAM_NAME

    def find_game_type_test(self):
        find_game_type(self.game_type_id, self.game_type_name)
