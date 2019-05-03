from dataclasses import dataclass

from app.models.armor_facing import ArmorFacing
from app.models.unit import Unit


@dataclass
class HeresyUnit(Unit):
    cost: str
    initiative: str
    unit_type: str
    armor_facing: ArmorFacing
