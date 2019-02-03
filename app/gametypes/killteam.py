from app.constants import KILLTEAM_NAME, KILLTEAM_ID
from app.gametypes.gametype import GameType


class KillTeam(GameType):
    game_type_name = KILLTEAM_NAME
    game_type_id = KILLTEAM_ID

    @property
    def return_name(self):
        return self.game_type_name

    def run_parser(self, game_type_name, game_type_id):
        pass
