from dataclasses import dataclass


@dataclass
class Unit:
    name: str = None
    wargear: dict = None
    abilities: dict = None
    movement: str = None
    weapon_skill: str = None
    ballistic_skill: str = None
    strength: str = None
    toughness: str = None
    wounds: str = None
    attacks: str = None
    leadership: str = None
    save: str = None
