from dataclasses import dataclass


@dataclass
class Weapon:
    name: str = ""
    range: str = ""
    weapon_type_name: str = ""
    weapon_type_value: str = ""
    strength: str = ""
    ap: str = ""
    damage: str = ""
    abilities: dict = ""
