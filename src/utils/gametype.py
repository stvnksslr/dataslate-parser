from bs4 import BeautifulSoup

from src.utils.constants import SUPPORTED_PARSERS, TEMPLATES


def detect_gametype(roster):
    soup = BeautifulSoup(roster, features="lxml")
    game_system = soup.find("roster").attrs.get("gamesystemid")
    return game_system


def find_gametype_parser(gametype):
    parser = SUPPORTED_PARSERS.get(gametype)
    if parser:
        return parser
    else:
        return "gametype not supported"


def find_template(gametype):
    template = TEMPLATES.get(gametype)
    return template
