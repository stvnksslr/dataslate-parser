from pydantic import BaseModel

from src.models.unit import Unit


class W40kSelection(BaseModel):
    name: str

    points: str | None = None
    power: str | None = None

    units: list

    wargear: dict | None = None

    rules: dict | None = None
    abilities: dict | None = None
    keywords: list
    psyker_powers: dict | None = None
    transport: dict | None = None


class W40kUnit(Unit):
    movement: str
