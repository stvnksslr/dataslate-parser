from typing import Optional

from src.models.armor_facing import ArmorFacing
from src.models.unit import Unit
from src.parsers.heresy.heresy_constants import STAT_BLOCK_TYPES


class HeresyUnit(Unit):
    initiative: Optional[str]
    unit_type: str
    armor_facing: Optional[ArmorFacing]
    stat_type: Optional[str]
    weapon: Optional[dict]

    @staticmethod
    def get_stat_type(unit_type):
        for category in STAT_BLOCK_TYPES:
            for stat_type in category.get("categories"):
                if unit_type == stat_type:
                    return category.get("name")
