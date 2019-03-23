from bs4 import BeautifulSoup

from app.models.unit import Unit


class UnitParser:
    @staticmethod
    def parse_units(contents):
        soup = BeautifulSoup(contents, "lxml")
        unit_list = soup.findAll("selection", {"type": "model"})
        parsed_unit_list = []

        for item in unit_list:
            parsed_unit_name = item.attrs.get('name')
            parsed_movement = item.contents[3].contents[1].contents[9].contents[1].attrs.get('value')
            parsed_unit = Unit(unit_name=parsed_unit_name,
                               movement=parsed_movement)
            parsed_unit_list.append(parsed_unit)
        return unit_list
