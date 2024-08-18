from types import ModuleType

from bs4 import BeautifulSoup

from src.utils.constants import SUPPORTED_PARSERS, TEMPLATES


def detect_gametype(roster):
    soup = BeautifulSoup(roster, features="xml")
    game_system = soup.find("roster").attrs.get("gameSystemId")
    return game_system


def find_gametype_parser(gametype) -> ModuleType | str:
    parser = SUPPORTED_PARSERS.get(gametype)
    if parser:
        return parser
    return "gametype not supported"


def find_template(gametype):
    template = TEMPLATES.get(gametype)
    return template
