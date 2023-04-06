from pydantic import BaseModel


class Unit(BaseModel):
    name: str
    wargear: dict
    abilities: dict
    weapon_skill: str | None
    ballistic_skill: str | None
    strength: str | None
    toughness: str | None
    wounds: str | None
    attacks: str | None
    leadership: str | None
    save: str | None
