from dataclasses import dataclass

from app.models.unit import Unit


@dataclass
class KtUnit(Unit):
    max: int
    role: str
    level: int
