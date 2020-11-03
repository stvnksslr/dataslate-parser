from dataclasses import dataclass

from src.models.armor_facing import ArmorFacing
from src.models.unit import Unit
from src.parsers.heresy.heresy_constants import STAT_BLOCK_TYPES


@dataclass
class HeresyUnit(Unit):
    initiative: str
    unit_type: str
    armor_facing: ArmorFacing
    stat_type: str
    weapon: list

    @staticmethod
    def get_stat_type(unit_type):
        for category in STAT_BLOCK_TYPES:
            for stat_type in category.get("categories"):
                if unit_type == stat_type:
                    return category.get("name")
