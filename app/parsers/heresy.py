from bs4 import BeautifulSoup

from app.models.heresy_unit import HeresyUnit
from app.models.unit_group import UnitGroup


def parse_units(contents):
    soup = BeautifulSoup(contents, "lxml")
    unit_list = soup.findAll("selection", {"type": "unit"})
    parsed_roster = create_list_of_units(unit_list)
    return parsed_roster


def create_list_of_units(unit_list):
    for item in unit_list:
        parsed_unit_group = []
        dict_of_abilities = get_abilities(item)
        parsed_unit = HeresyUnit(abilities=dict_of_abilities)
        parsed_unit_group.append(parsed_unit)
        parsed_unit_group = UnitGroup(name='placeholder', list_of_units=parsed_unit_group)
        return parsed_unit_group


def get_abilities(item):
    dict_of_abilities = {}

    list_of_abilities_v2 = item.findAll('description')
    for ability in list_of_abilities_v2:
        ability_name = ability.parent.attrs.get('name')
        ability_description = str(ability.contents[0]).rstrip()
        dict_of_abilities.update({ability_name: ability_description})

    return dict_of_abilities
