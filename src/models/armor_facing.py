from dataclasses import dataclass


@dataclass
class ArmorFacing:
    front: str | None
    side: str | None
    rear: str | None
    hp: str | None
