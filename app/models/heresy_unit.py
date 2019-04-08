from dataclasses import dataclass

from app.models.unit import Unit


@dataclass
class HeresyUnit(Unit):
    cost: str = None
    number_of_units: str = None
    initiative: str = None
    unit_type: str = None
