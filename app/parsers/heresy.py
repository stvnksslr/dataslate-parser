from bs4 import BeautifulSoup

from app.models.heresy_unit import HeresyUnit
from app.models.unit_group import UnitGroup


def parse_units(contents):
    soup = BeautifulSoup(contents, "lxml")
    unit_list = soup.findAll("selection", {"type": "unit"})
    parsed_roster = create_unit(unit_list)
    return parsed_roster


def create_unit(unit_list):
    list_of_units = []
    for item in unit_list:
        dict_of_abilities = get_abilities(item)
        unit_group_name = get_unit_group_name(item)
        list_of_units_in_group = item.findAll("profile", {"profiletypename": "Unit"})
        parsed_list_if_units_in_group = get_units_in_group(list_of_units_in_group, dict_of_abilities)
        parsed_group = UnitGroup(name=unit_group_name, list_of_units=parsed_list_if_units_in_group)
        list_of_units.append(parsed_group)

    return list_of_units


def get_units_in_group(list_of_units_in_group, dict_of_abilities):
    parsed_units_in_group = []
    for unit in list_of_units_in_group:
        create_unit_object(dict_of_abilities, parsed_units_in_group, unit)
    return parsed_units_in_group


def create_unit_object(dict_of_abilities, parsed_units_in_group, unit):
    unit_name = unit.attrs.get('name')
    unit_count = unit.parent.parent.attrs.get('number')
    list_of_unit_characteristics = unit.findAll('characteristic')
    dict_of_characteristics = get_unit_characteristics(list_of_unit_characteristics)
    parsed_unit = HeresyUnit(name=unit_name,
                             number_in_unit=unit_count,
                             unit_type=dict_of_characteristics.get('Unit Type'),
                             weapon_skill=dict_of_characteristics.get("WS"),
                             ballistic_skill=dict_of_characteristics.get("BS"),
                             strength=dict_of_characteristics.get("S"),
                             toughness=dict_of_characteristics.get("T"),
                             wounds=dict_of_characteristics.get("W"),
                             initiative=dict_of_characteristics.get("I"),
                             attacks=dict_of_characteristics.get("A"),
                             leadership=dict_of_characteristics.get("LD"),
                             save=dict_of_characteristics.get('Save'),
                             abilities=dict_of_abilities)
    parsed_units_in_group.append(parsed_unit)


def get_unit_characteristics(list_of_unit_characteristics):
    dict_of_characteristics = {}
    for characteristic in list_of_unit_characteristics:
        characteristic_name = characteristic.attrs.get('name')
        characteristic_value = characteristic.attrs.get('value')
        dict_of_characteristics.update({characteristic_name: characteristic_value})
    return dict_of_characteristics


def get_unit_group_name(item):
    return item.attrs.get('name')


def get_abilities(item):
    dict_of_abilities = {}
    list_of_abilities_v2 = item.findAll('description')
    for ability in list_of_abilities_v2:
        ability_name = ability.parent.attrs.get('name')
        ability_description = str(ability.contents[0]).rstrip()
        dict_of_abilities.update({ability_name: ability_description})
    return dict_of_abilities
