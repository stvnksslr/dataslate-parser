from src.models.unit import Unit


class KillteamUnit(Unit):
    movement: str
    apl: str
    ga: str
    df: str
    keywords: list
    psyker_powers: dict | None = None
