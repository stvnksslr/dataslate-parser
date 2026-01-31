from types import ModuleType

from bs4 import BeautifulSoup, Tag

from src.utils.constants import SUPPORTED_PARSERS, TEMPLATES


def detect_gametype(roster) -> str | None:
    soup = BeautifulSoup(roster, features="xml")
    roster_element = soup.find("roster")
    if not isinstance(roster_element, Tag):
        return None
    game_system = roster_element.attrs.get("gameSystemId")
    return game_system


def find_gametype_parser(gametype) -> ModuleType | str:
    parser = SUPPORTED_PARSERS.get(gametype)
    if parser:
        return parser
    return "gametype not supported"


def find_template(gametype):
    template = TEMPLATES.get(gametype)
    return template
