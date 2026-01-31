from bs4 import BeautifulSoup, Tag

from src.utils.constants import SUPPORTED_BATTLESCRIBE_VERSION


def check_battlescribe_version(roster) -> bool:
    soup = BeautifulSoup(roster, features="xml")
    roster_element = soup.find("roster")
    if not isinstance(roster_element, Tag):
        return False
    battlescribe_version = roster_element.attrs.get("battleScribeVersion")
    if battlescribe_version is None:
        return False
    return battlescribe_version >= SUPPORTED_BATTLESCRIBE_VERSION
