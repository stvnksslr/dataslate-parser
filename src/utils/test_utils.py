from bs4 import BeautifulSoup
from src.utils.gametype import detect_gametype, find_gametype_parser, find_template


def fetch_and_parse_roster(roster_file):
    with open(roster_file, "r") as roster_file:
        roster_file = roster_file.read()

        return get_parser_type_and_parse(roster_file, False).get('roster')


def fetch_and_parse_rules(roster_file):
    with open(roster_file, "r") as roster_file:
        roster_file = roster_file.read()

        return get_parser_type_and_parse(roster_file, True).get('rules_summary')


def get_parser_type_and_parse(roster, summary_page):
    soup = BeautifulSoup(roster, features="lxml")

    gametype = detect_gametype(roster)
    parser = find_gametype_parser(gametype)
    parsed_roster = parser.parse_units(soup)

    rules_summary = {}
    if summary_page:
        rules_summary = parser.get_rules_summary(parsed_roster, soup)

    template = find_template(gametype)

    return {"roster": parsed_roster, "template": template, "rules_summary": rules_summary}
