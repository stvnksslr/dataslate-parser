from dataclasses import dataclass
from src.models.unit import Unit


@dataclass
class KillteamUnit(Unit):
    movement: str
    max_allowed: str = None
    keywords: list = None
    psyker_powers: dict = None
    point_cost: int = 0
