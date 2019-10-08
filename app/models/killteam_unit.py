import json
from dataclasses import dataclass, asdict

from app.models.unit import Unit


@dataclass
class KillteamUnit(Unit):
    max: str = None
    keywords: list = None
    point_cost: int = 0
