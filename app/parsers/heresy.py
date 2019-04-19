from bs4 import BeautifulSoup

from app.models.armor_facing import ArmorFacing
from app.models.heresy_unit import HeresyUnit
from app.models.unit_group import UnitGroup


def parse_units(contents):
    soup = BeautifulSoup(contents, "lxml")
    list_of_parsable_items = soup.find('selections').contents
    cleaned_item_to_parse = [parsable_item for parsable_item in list_of_parsable_items if parsable_item != '\n']
    list_of_units = get_units(cleaned_item_to_parse)
    list_of_upgrades = get_upgrades(cleaned_item_to_parse)

    parsed_upgrades = parse_upgrades(list_of_upgrades)
    parsed_units = create_unit(list_of_units)
    parsed_roster = [parsed_upgrades, parsed_units]
    return parsed_roster


def parse_upgrades(list_of_upgrades):
    dict_of_upgrades = {}
    for upgrade in list_of_upgrades:
        upgrade_name = upgrade.attrs.get('name')
        upgrade_description = upgrade.find('description')
        # this can sometimes be blank
        if upgrade_description:
            upgrade_description = upgrade_description.contents[0]

        dict_of_upgrades.update({upgrade_name: upgrade_description})
    parsed_upgrades = dict_of_upgrades
    return parsed_upgrades


def get_units(cleaned_item_to_parse):
    list_of_units = []
    for item in cleaned_item_to_parse:
        if item.attrs.get('type') == 'model' or item.attrs.get('type') == 'unit':
            list_of_units.append(item)
    return list_of_units


def get_upgrades(cleaned_item_to_parse):
    list_of_upgrades = []
    for item in cleaned_item_to_parse:
        if item.attrs.get('type') == 'upgrade':
            list_of_upgrades.append(item)
    return list_of_upgrades


def create_unit(unit_list):
    list_of_units = []
    for item in unit_list:
        dict_of_abilities = get_abilities(item)
        unit_group_name = get_unit_group_name(item)
        dict_of_wargear = get_wargear(item)
        list_of_units_in_group = item.findAll("profile", {"profiletypename": "Unit"})
        list_of_vehicles_in_group = item.findAll("profile", {"profiletypename": 'Vehicle'})
        list_of_models_as_units = item.findAll("selection", {"type": 'model'})
        list_to_be_parsed = list_of_units_in_group

        if not list_of_units_in_group:
            list_to_be_parsed = list_of_vehicles_in_group

        if not list_of_vehicles_in_group and not list_of_units_in_group:
            list_to_be_parsed = list_of_models_as_units

        if not list_of_vehicles_in_group and not list_of_units_in_group and not list_of_models_as_units:
            raw_list_of_upgrades_as_units = item.find('selections').contents
            list_of_upgrades_as_units = [raw_list_of_upgrades_as_units for raw_list_of_upgrades_as_units in
                                         raw_list_of_upgrades_as_units if
                                         raw_list_of_upgrades_as_units.name]

            list_to_be_parsed = list_of_upgrades_as_units

        dedicated_transport = item.findAll("category", {"name": "Dedicated Transport"})
        transport = item.findAll("category", {"name": "Transport"})

        if transport and dedicated_transport:
            list_to_be_parsed.append(transport[0].parent.parent)

        elif transport:
            list_to_be_parsed.append(transport[0].parent.parent)

        elif dedicated_transport:
            list_to_be_parsed.append(dedicated_transport[0].parent.parent)

        parsed_list_if_units_in_group = parse_items_in_group(list_to_be_parsed, dict_of_abilities, dict_of_wargear)
        parsed_group = UnitGroup(name=unit_group_name, list_of_units=parsed_list_if_units_in_group)
        list_of_units.append(parsed_group)

    return list_of_units


def get_wargear(item):
    list_of_potential_wargear = item.findAll('profile', {'profiletypename': 'Weapon'})
    dict_of_wargear = {}
    for wargear in list_of_potential_wargear:
        wargear_name = wargear.attrs.get('name')
        if hasattr(wargear.find('characteristics'), 'contents'):
            list_of_wargear_stats = wargear.find('characteristics').contents
            cleaned_list_of_wargear_stats = [list_of_wargear_stats for list_of_wargear_stats in
                                             list_of_wargear_stats if
                                             list_of_wargear_stats != '\n']
            wargear_dict = get_unit_characteristics(cleaned_list_of_wargear_stats)
            dict_of_wargear.update({wargear_name: wargear_dict})
    return dict_of_wargear


def parse_items_in_group(list_of_units_in_group, dict_of_abilities, dict_of_wargear):
    parsed_units_in_group = []
    for unit in list_of_units_in_group:
        create_unit_object(dict_of_abilities, parsed_units_in_group, unit, dict_of_wargear)
    return parsed_units_in_group


def create_unit_object(dict_of_abilities, parsed_units_in_group, unit, dict_of_wargear):
    unit_name = unit.attrs.get('name')
    unit_count = unit.parent.parent.attrs.get('number')
    list_of_unit_characteristics = unit.find('characteristics').contents
    cleaned_list_of_unit_characteristic = [list_of_unit_characteristics for list_of_unit_characteristics in
                                           list_of_unit_characteristics
                                           if list_of_unit_characteristics != '\n']

    if bool(unit.findAll("profile", {"profiletypename": "Vehicle"})):
        possible_vehicle_characteristics = unit.findAll("profile", {"profiletypename": "Vehicle"})[0]
        list_of_vehicle_characteristics = possible_vehicle_characteristics.find('characteristics').contents
        cleaned_list_of_vehicle_characteristics = \
            [list_of_vehicle_characteristics for list_of_vehicle_characteristics in
             list_of_vehicle_characteristics
             if list_of_vehicle_characteristics != '\n']

        for characteristic in cleaned_list_of_vehicle_characteristics:
            cleaned_list_of_unit_characteristic.append(characteristic)

    dict_of_characteristics = get_unit_characteristics(cleaned_list_of_unit_characteristic)

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
                             abilities=dict_of_abilities,
                             wargear=dict_of_wargear,
                             armor_facing=ArmorFacing(front=dict_of_characteristics.get('Front'),
                                                      side=dict_of_characteristics.get('Side'),
                                                      rear=dict_of_characteristics.get('Rear'),
                                                      hp=dict_of_characteristics.get('HP')))
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
