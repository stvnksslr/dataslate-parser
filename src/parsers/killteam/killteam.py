from bs4 import BeautifulSoup

from src.models.killteam_unit import KillteamUnit


def parse_units(roster_file):
    soup = BeautifulSoup(roster_file, features="lxml")
    operative_list = soup.find_all("profile", {"typename": "Operative"})
    parsed_unit_list = create_list_of_units(operative_list)
    return parsed_unit_list


def create_list_of_units(model_list):
    parsed_models = []
    for model in model_list:
        name = get_model_name(model)
        characteristics = get_characteristics(model)
        wargear = get_item_details(model, "Weapons")
        keywords = get_keywords(model)
        abilities = get_rules(model)

        parsed_model = KillteamUnit(
            name=name,
            movement=characteristics.get("M"),
            apl=characteristics.get("APL"),
            ga=characteristics.get("GA"),
            df=characteristics.get("DF"),
            save=characteristics.get("SV"),
            wounds=characteristics.get("W"),
            keywords=keywords,
            wargear=wargear,
            abilities=abilities,
        )
        parsed_models.append(parsed_model)

    return parsed_models


def get_rules(model):
    list_of_rules = model.parent.parent.find_all("rule")
    dict_of_abilities = {}
    for rule in list_of_rules:
        name = rule.attrs.get("name")
        value = rule.text.strip('\n')
        dict_of_abilities.update({name: value})
    return dict_of_abilities


def get_keywords(model):
    categories = []
    list_of_categories = model.parent.parent.find_all("category")
    for category in list_of_categories:
        categories.append(category.attrs.get("name"))
    return categories


def get_item_details(model, search_type):
    search_filter = model.parent.parent.find_all("profile", {"typename": search_type})
    formatted_items = {}

    for item in search_filter:
        stats = item.find_all("characteristic")
        item_name = item.attrs.get("name")
        characteristic_dict = {}

        for characteristic in stats:
            name = characteristic.attrs.get("name")
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
            elif name in ["M", "APL", "GA", "DF", "W", "SV"]:
                dict_of_characteristics.update({name: value})
    return dict_of_characteristics
