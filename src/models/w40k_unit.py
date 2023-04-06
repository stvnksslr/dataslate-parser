from pydantic import BaseModel

from src.models.unit import Unit


class W40kSelection(BaseModel):
    name: str

    points: str = None
    power: str = None

    units: list

    wargear: dict = None

    rules: dict = None
    abilities: dict = None
    keywords: list
    psyker_powers: dict | None
    transport: dict | None


class W40kUnit(Unit):
    movement: str
