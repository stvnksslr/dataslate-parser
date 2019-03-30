from dataclasses import asdict

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
            unit_profile = UnitParser.fetch_list_of_profiles(item, parsed_unit_name)
            list_of_attributes = UnitParser.list_of_attributes(unit_profile)

            parsed_unit = Unit(unit_name=parsed_unit_name,
                               movement=list_of_attributes.get('M'),
                               weapon_skill=list_of_attributes.get('WS'),
                               ballistic_skill=list_of_attributes.get('BS'),
                               strength=list_of_attributes.get('S'),
                               toughness=list_of_attributes.get('T'),
                               wounds=list_of_attributes.get('W'),
                               attacks=list_of_attributes.get('A'),
                               leadership=list_of_attributes.get('L'),
                               save=list_of_attributes.get("SV"),
                               max=list_of_attributes.get("MAX")
                               )
            parsed_unit_list.append(parsed_unit)

        return unit_list

    @staticmethod
    def fetch_list_of_profiles(item, parsed_unit_name):
        unit_profile = [item for item in item.contents
                        if item.name == "profiles"][0].contents

        specific_unit_profile = [unit_profile for unit_profile in unit_profile
                                 if unit_profile.name == "profile" if
                                 unit_profile.attrs.get('name') == parsed_unit_name][0].contents

        list_of_characteristics = [selected_unit for selected_unit in specific_unit_profile
                                   if selected_unit.name == "characteristics"][0].contents

        cleaned_list_of_characteristics = [selected_unit for selected_unit in list_of_characteristics if
                                           selected_unit.name == "characteristic"]

        return cleaned_list_of_characteristics

    @staticmethod
    def list_of_attributes(item):
        list_of_attrs = {}
        for attribute in item:
            attr_name = attribute.get('name')
            attr_value = attribute.get('value')
            list_of_attrs.update({attr_name: attr_value})
        return list_of_attrs
