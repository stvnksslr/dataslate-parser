from dataclasses import dataclass


@dataclass
class Weapon:
    name: str
    range: int
    weapon_type_name: str
    weapon_type_value: int
    strength: int
    ap: int
    damage: int
    abilities: dict
