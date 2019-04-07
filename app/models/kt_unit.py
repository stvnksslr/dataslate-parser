from dataclasses import dataclass

from app.models.unit import Unit


@dataclass
class KtUnit(Unit):
    max: str = ""
    keywords: list = ""
    point_cost: int = 0
