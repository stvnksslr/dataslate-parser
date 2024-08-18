from dataclasses import dataclass


@dataclass
class UnitGroup:
    name: str | None = None
    list_of_units: list | None = None
    toughness: list | None = None
    armored: list | None = None
    hybrid: list | None = None
