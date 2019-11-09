from app.utils.gametype import detect_gametype, find_gametype_parser, find_template


def fetch_and_parse_roster(roster_file):
    with open(roster_file, "r") as roster_file:
        roster_file = roster_file.read()
        gametype = detect_gametype(roster_file)
        parser = find_gametype_parser(gametype)
        parsed_roster = parser.parse_units(roster_file=roster_file)
        return parsed_roster


def get_parser_type_and_parse(roster):
    gametype = detect_gametype(roster)
    parser = find_gametype_parser(gametype)
    template = find_template(gametype)

    parsed_roster = parser.parse_units(roster_file=roster)
    return {"roster": parsed_roster, "template": template}
