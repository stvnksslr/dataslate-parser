from dataclasses import dataclass
from typing import Optional


@dataclass
class ArmorFacing:
    front: Optional[str]
    side: Optional[str]
    rear: Optional[str]
    hp: Optional[str]
