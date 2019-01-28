supported_gametypes = {
    killteam:KillTeam
}


def find_gametype(self, gametype, gametype_id):
    self.gametype = gametype
    self.gametype_id = gametype_id
    if self.gametype == supported_gametypes:
        return True
    else:
        return False
