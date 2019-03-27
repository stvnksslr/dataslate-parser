from dataclasses import asdict

from bs4 import BeautifulSoup

from app.models.characteristics import Characteristic
from app.models.unit import Unit


# movement
# parsed_movement = item.contents[3].contents[1].contents[9].contents[1].attrs.get('value')

class UnitParser:
    @staticmethod
    def parse_units(contents):
        soup = BeautifulSoup(contents, "lxml")
        unit_list = soup.findAll("selection", {"type": "model"})
        parsed_unit_list = []

        for item in unit_list:
            parsed_unit_name = item.attrs.get('name')
            parsed_unit = Unit(unit_name=parsed_unit_name)
            UnitParser.parse_characteristics(item.contents[3])
            parsed_unit_list.append(parsed_unit)

        return unit_list

    @staticmethod
    def parse_characteristics(item):
        parsed_characteristics = item.findAll('characteristic')
        for characteristic in parsed_characteristics:
            list_of_characteristics = characteristic.attrs.get('value')
            for characteristic_value in list_of_characteristics:
                characteristic_value.append()
