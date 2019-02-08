from bs4 import BeautifulSoup
from app.models.kt_models import kt_unit

class UnitParser:
    @staticmethod
    def parse_units(contents):
        soup = BeautifulSoup(contents, "html")
        unit_list = soup.findAll("selection", {"type": "model"})
        for unit in unit_list:
            unit_name = unit.attrs.get('name')
        return unit_list
