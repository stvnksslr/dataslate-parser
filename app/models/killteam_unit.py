from dataclasses import dataclass

from app.models.unit import Unit


@dataclass
class KillteamUnit(Unit):
    max: str = None
    keywords: list = None
    point_cost: int = 0
