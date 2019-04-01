from bs4 import BeautifulSoup
from app.models.unit import Unit


class UnitParser:
    @staticmethod
    def parse_units(contents):
        soup = BeautifulSoup(contents, "lxml")
        unit_list = soup.findAll("selection", {"type": "model"})
        parsed_unit_list = []
        UnitParser.get_unit_stats(parsed_unit_list, unit_list)
        return parsed_unit_list

    @staticmethod
    def get_unit_stats(parsed_unit_list, unit_list):
        for item in unit_list:
            parsed_unit_name = item.attrs.get("name")
            unit_profile = UnitParser.fetch_list_of_profiles(item, parsed_unit_name)
            list_of_attributes = UnitParser.dict_of_attributes(unit_profile)
            list_of_keywords = UnitParser.get_keywords(item)
            list_of_weapons = UnitParser.get_weapons(item)
            dict_of_wargear = {}
            for weapon in list_of_weapons:
                dict_of_wargear.update({weapon.get("Name"): weapon})

            parsed_unit = Unit(
                unit_name=parsed_unit_name,
                movement=list_of_attributes.get("M"),
                weapon_skill=list_of_attributes.get("WS"),
                ballistic_skill=list_of_attributes.get("BS"),
                strength=list_of_attributes.get("S"),
                toughness=list_of_attributes.get("T"),
                wounds=list_of_attributes.get("W"),
                attacks=list_of_attributes.get("A"),
                leadership=list_of_attributes.get("L"),
                save=list_of_attributes.get("Sv"),
                max=list_of_attributes.get("Max"),
                keywords=list_of_keywords,
                wargear=dict_of_wargear,
            )

            parsed_unit_list.append(parsed_unit)

    @staticmethod
    def get_weapons(item):
        weapons = [item for item in item.contents if item.name == "selections"][0].contents
        list_of_weapons = []
        cleaned_weapons = [weapons for weapons in weapons if weapons.name]
        list_of_cleaned_weapon_stats = [cleaned_weapons.contents for cleaned_weapons in cleaned_weapons]

        for weapon in list_of_cleaned_weapon_stats:
            weapon_profile = [weapon for weapon in weapon if weapon.name if weapon.name == "profiles"]
            test = [weapon_profile.contents for weapon_profile in weapon_profile][0]
            test2 = [test for test in test if test.name]

            for weapon_ in test2:
                weapon_name = weapon_.attrs.get("name")
                weapon_profile_cleaned = [weapon_ for weapon_ in weapon_ if weapon_.name == "characteristics"][0]

                weapon_profile_cleaned_list = [
                    weapon_profile_cleaned
                    for weapon_profile_cleaned in weapon_profile_cleaned
                    if weapon_profile_cleaned.name == "characteristic"
                ]

                parsed_weapons = UnitParser.dict_of_attributes(weapon_profile_cleaned_list)
                parsed_weapons.update({"Name": weapon_name})
                list_of_weapons.append(parsed_weapons)
        return list_of_weapons

    @staticmethod
    def get_keywords(item):
        keyword_list = []
        keywords = [item for item in item.contents if item.name == "categories"][0].contents
        cleaned_keywords = [keyword for keyword in keywords if keyword.name]
        for keyword in cleaned_keywords:
            keyword_list.append(keyword.attrs.get("name"))
        return keyword_list

    @staticmethod
    def fetch_list_of_profiles(item, parsed_unit_name):
        unit_profile = [item for item in item.contents if item.name == "profiles"][0].contents

        specific_unit_profile = [
            unit_profile
            for unit_profile in unit_profile
            if unit_profile.name == "profile"
            if unit_profile.attrs.get("name") == parsed_unit_name][0].contents

        list_of_characteristics = [
            selected_unit
            for selected_unit in specific_unit_profile
            if selected_unit.name == "characteristics"][0].contents

        cleaned_list_of_characteristics = [
            selected_unit
            for selected_unit in list_of_characteristics
            if selected_unit.name == "characteristic"]

        return cleaned_list_of_characteristics

    @staticmethod
    def dict_of_attributes(item):
        dict_of_attrs = {}
        for attribute in item:
            attr_name = attribute.get("name")
            attr_value = attribute.get("value")
            dict_of_attrs.update({attr_name: attr_value})
        return dict_of_attrs
