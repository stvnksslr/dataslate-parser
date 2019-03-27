from dataclasses import dataclass

from app.models.unit import Unit


@dataclass
class Characteristic:
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
