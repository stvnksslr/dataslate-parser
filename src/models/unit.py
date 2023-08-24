from pydantic import BaseModel


class Unit(BaseModel):
    name: str
    wargear: dict
    abilities: dict
    weapon_skill: str | None = None
    ballistic_skill: str | None = None
    strength: str | None = None
    toughness: str | None = None
    wounds: str | None = None
    attacks: str | None = None
    leadership: str | None = None
    save: str | None = None
