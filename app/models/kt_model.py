from dataclasses import dataclass

from app.models.model import Model


@dataclass
class KtModel(Model):
    max: str = None
    keywords: list = None
    point_cost: int = 0
