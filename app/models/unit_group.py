from dataclasses import dataclass


@dataclass
class UnitGroup:
    name: str = None
    list_of_units: list = None
    toughness: list = None
    armored: list = None
    hybrid: list = None
