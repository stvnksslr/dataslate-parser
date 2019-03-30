from dataclasses import dataclass


@dataclass
class Unit:
    unit_name: str = ""
    wargear: dict = ""
    abilities: dict = ""
    keywords: dict = ""
    point_cost: int = 0
    movement: int = 0
    weapon_skill: int = 0
    ballistic_skill: int = 0
    strength: int = 0
    toughness: int = 0
    wounds: int = 0
    attacks: int = 0
    leadership: int = 0
    save: int = 0
    max: int = 0
