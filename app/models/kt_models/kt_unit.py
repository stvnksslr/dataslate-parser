from dataclasses import dataclass


@dataclass
class KtUnit:
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
    max: int
    role: str
    level: int
    point_cost: int
    wargear: dict
    abilities: dict
    keywords: dict
