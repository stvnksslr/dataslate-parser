from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel


class Unit(BaseModel):
    name: str
    wargear: dict
    abilities: dict
    weapon_skill: Optional[str]
    ballistic_skill: Optional[str]
    strength: Optional[str]
    toughness: Optional[str]
    wounds: Optional[str]
    attacks: Optional[str]
    leadership: Optional[str]
    save: Optional[str]
