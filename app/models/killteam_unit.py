import json
from dataclasses import dataclass, asdict

from app.models.unit import Unit


@dataclass
class KillteamUnit(Unit):
    max: str = None
    keywords: list = None
    point_cost: int = 0

    def to_json(self):
        json.dumps(asdict(self))
