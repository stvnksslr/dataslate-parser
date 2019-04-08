from dataclasses import dataclass

from app.models.unit import Unit


@dataclass
class HeresyUnit(Unit):
    cost: str = None
    number_in_unit: str = 1
    initiative: str = None
    unit_type: str = None
    movement: str = '6"'
