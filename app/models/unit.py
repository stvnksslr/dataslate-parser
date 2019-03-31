from dataclasses import dataclass


@dataclass
class Unit:
    unit_name: str = ""
    wargear: list = ""
    abilities: dict = ""
    keywords: list = ""
    point_cost: int = 0
    movement: str = ""
    weapon_skill: str = ""
    ballistic_skill: str = ""
    strength: str = ""
    toughness: str = ""
    wounds: str = ""
    attacks: str = ""
    leadership: str = ""
    save: str = ""
    max: str = ""
