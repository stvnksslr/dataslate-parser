from dataclasses import dataclass


@dataclass
class Unit:
    unit_name: str = ""
    wargear: dict = ""
    abilities: dict = ""
    keywords: dict = ""
    point_cost: int = 0
