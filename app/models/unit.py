from dataclasses import dataclass


@dataclass
class Unit:
    unit_name: str
    movement: int
    weapon_skill: int
    ballistic_skill: int
    strength: int
    toughness: int
    wounds: int
    attacks: int
    leadership: int
    save: int
    wargear: dict
    abilities: dict
    keywords: dict
    point_cost: int
