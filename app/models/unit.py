from dataclasses import dataclass


@dataclass
class Unit:
    name: str = ""
    wargear: dict = ""
    abilities: dict = ""
    movement: str = ""
    weapon_skill: str = ""
    ballistic_skill: str = ""
    strength: str = ""
    toughness: str = ""
    wounds: str = ""
    attacks: str = ""
    leadership: str = ""
    save: str = ""
