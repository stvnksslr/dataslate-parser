from bs4 import BeautifulSoup

from app.models.armor_facing import ArmorFacing
from app.models.heresy_unit import HeresyUnit
from app.models.unit_group import UnitGroup


def parse_units(contents):
    rule_whitelist = ['Rite of War', 'Legion and Allegiance', 'Use Playtest Rules']
    soup = BeautifulSoup(contents, "lxml")
    selections = soup.find('selections').find_all('selection', recursive=False)

    rules = filter_out_rules(rule_whitelist, selections)
    squads = selections
    list_of_squads = get_squads(squads)

    parsed_list = create_parsed_list(list_of_squads)

    return parsed_list


def create_parsed_list(list_of_squads):
    parsed_list = []
    for squads in list_of_squads:
        for unit in squads:
            parsed_model = HeresyUnit(
                name=unit.get('name'),
                unit_type=unit.get('unit type'),
                weapon_skill=unit.get('ws'),
                ballistic_skill=unit.get('bs'),
                strength=unit.get('s'),
                toughness=unit.get('t'),
                wounds=unit.get('w'),
                initiative=unit.get('i'),
                attacks=unit.get('a'),
                leadership=unit.get('ld'),
                save=unit.get('save'),
                wargear=None,
                abilities=None,
                movement=None,
                cost=None,
                armor_facing=ArmorFacing(front=unit.get('front'),
                                         side=unit.get('side'),
                                         rear=unit.get('rear'),
                                         hp=unit.get('hp'))
            )
            parsed_list.append(parsed_model)
    return parsed_list


def get_squads(squads):
    list_of_squads = []
    for unit in squads:
        list_of_squads.append(parse_squad_characteristics(unit))
    return list_of_squads


def parse_squad_characteristics(unit):
    parsed_profiles = []
    unit_name = unit.attrs.get('name')
    list_of_units = unit.find_all(typename="Unit")
    list_of_walkers = unit.find_all(typename='Walker')
    list_of_vehicles = unit.find_all(typename='Vehicle')
    list_of_profiles_in_squad = list_of_units + list_of_walkers + list_of_vehicles
    for profile in list_of_profiles_in_squad:
        parsed_profiles.append(get_characteristics(profile, unit_name))
    return parsed_profiles


def get_characteristics(unit_type, unit_name):
    dict_of_characteristics = {}
    dict_of_characteristics.update({"unit_name": unit_name})
    model_name = unit_type.attrs.get('name').lower()
    dict_of_characteristics.update({'name': model_name})
    unit_characteristics = unit_type.find_all('characteristic')
    for characteristic in unit_characteristics:
        name = characteristic.attrs.get('name').lower()
        value = characteristic.contents[0].lower()
        dict_of_characteristics.update({name: value})
    return dict_of_characteristics


def filter_out_rules(rule_whitelist, selections):
    dict_of_rules = {}
    for rule in rule_whitelist:
        for idx, selection in enumerate(selections):
            name = selection.attrs.get('name')
            if name == rule:
                dict_of_rules.update({name: selection})
                selections.pop(idx)
    return dict_of_rules
