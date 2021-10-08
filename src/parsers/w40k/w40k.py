from bs4 import BeautifulSoup

from src.models.w40k_unit import W40kSelection, W40kUnit


def parse_units(roster_file):
    parsed_units = []
    soup = BeautifulSoup(roster_file, features="lxml")

    forces = soup.find_all("force")
    for force in forces:
        for selection in force.selections.children:

            if str(selection).strip() == "":
                continue

            if selection.attrs.get("type") in ["model", "unit"]:
                parsed_units.append(parse_selection(selection))

    return parsed_units


def parse_selection(unit):
    unit_name = get_model_name(unit)

    units = []

    res = create_list_of_units(unit.find_all("profile", {"type": "model"}))
    if len(res) > 0:
        units.extend(res)

    res = create_list_of_units(unit.find_all("profile", {"typename": "Unit"}))
    if len(res) > 0:
        units.extend(res)

    wargear = get_item_details(unit, "Weapon")

    keywords = get_keywords(unit)
    rules = get_rules(unit)
    abilities = get_abilities(unit)

    psyker_powers = get_psychic(unit)

    parsed_unit = W40kSelection(
        name=unit_name,
        units=units,
        keywords=keywords,
        rules=rules,
        abilities=abilities,
        wargear=wargear,
        psyker_powers=psyker_powers
    )

    return parsed_unit


def create_list_of_units(model_list):
    parsed_models = []
    for model in model_list:

        unit_name = get_model_name(model)

        characteristics = get_characteristics(model)

        parsed_model = W40kUnit(
            name=unit_name,
            movement=characteristics.get("M"),
            weapon_skill=characteristics.get("WS"),
            ballistic_skill=characteristics.get("BS"),
            strength=characteristics.get("S"),
            toughness=characteristics.get("T"),
            wounds=characteristics.get("W"),
            attacks=characteristics.get("A"),
            leadership=characteristics.get("Ld"),
            save=characteristics.get("Save"),
            keywords=[],
            wargear={},
            abilities={},
        )
        parsed_models.append(parsed_model)

    return parsed_models


def get_rules(model):
    list_of_rules = model.find_all("rule")
    dict_of_rules = {}
    for rule in list_of_rules:
        name = rule.attrs.get("name")
        value = rule.text.strip("\n")
        dict_of_rules.update({name: value})
    return dict_of_rules


def get_abilities(model):
    list_of_rules = model.find_all("profile", {"typename": "Abilities"})
    dict_of_rules = {}
    for rule in list_of_rules:
        name = rule.attrs.get("name")
        value = rule.text.strip("\n")
        dict_of_rules.update({name: value})
    return dict_of_rules


def get_keywords(model):
    categories = []
    list_of_categories = model.find_all("category")
    for category in list_of_categories:
        categories.append(category.attrs.get("name"))
    return categories


def get_item_details(model, search_type):
    search_filter = model.find_all("profile", {"typename": search_type})
    formatted_items = {}

    for item in search_filter:
        stats = item.find_all("characteristic")
        item_name = item.attrs.get("name")
        characteristic_dict = {}

        for characteristic in stats:
            name = characteristic.attrs.get("name")
            value = ""
            if len(characteristic.contents) > 0:
                value = characteristic.contents[0]
            characteristic_dict.update({name: value})

        formatted_items.update({item_name: characteristic_dict})

    return formatted_items


def get_psychic(model):
    search_filter = model.find_all("profile", {"typename": "Psychic Power"})
    formatted_items = {}

    for item in search_filter:
        stats = item.find_all("characteristic")
        item_name = item.attrs.get("name")
        characteristic_dict = {}

        for characteristic in stats:
            name = characteristic.attrs.get("name").replace(" ", "_")
            value = ""
            if len(characteristic.contents) > 0:
                value = characteristic.contents[0]
            characteristic_dict.update({name: value})

        formatted_items.update({item_name: characteristic_dict})

    return formatted_items


def get_model_name(model):
    return model.attrs.get("name")


def get_characteristics(model):
    dict_of_characteristics = {}
    model_profile = model.find_all("characteristic")
    if bool(model_profile):
        for characteristic in model_profile:
            name = characteristic.attrs.get("name")
            value = characteristic.contents[0]
            if name == "Equipment":
                pass
            elif name in ["M", "WS", "BS", "S", "T", "W", "A", "Ld", "Save"]:
                dict_of_characteristics.update({name: value})
    return dict_of_characteristics
