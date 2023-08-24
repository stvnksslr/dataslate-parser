from src.models.armor_facing import ArmorFacing
from src.models.unit import Unit
from src.parsers.heresy.heresy_constants import STAT_BLOCK_TYPES


class HeresyUnit(Unit):
    initiative: str | None = None
    unit_type: str
    armor_facing: ArmorFacing | None = None
    stat_type: str | None = None
    weapon: dict | None = None
    move: str | None = None

    @staticmethod
    def get_stat_type(unit_type):
        for category in STAT_BLOCK_TYPES:
            for stat_type in category.get("categories", {}):
                if unit_type == stat_type:
                    return category.get("name", {})
        return None
