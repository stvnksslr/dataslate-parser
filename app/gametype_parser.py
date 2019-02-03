from app.gametypes import killteam
from app.gametypes.killteam import KillTeam

supported_game_types = {
    killteam: KillTeam
}


def find_game_type(self, game_type_name, game_type_id):
    self.game_type_name = game_type_name
    self.game_type_id = game_type_id

    if self.game_type_name == supported_game_types.get('game_type_name'):
        return True
    else:
        return False
