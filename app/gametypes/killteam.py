from app.constants import KILLTEAM_NAME, KILLTEAM_ID
from app.gametypes.gametype import GameType


class KillTeam(GameType):
    gametype_name = KILLTEAM_NAME
    gametype_id = KILLTEAM_ID

    def find(self, gametype_name, gametype_id):
        pass
