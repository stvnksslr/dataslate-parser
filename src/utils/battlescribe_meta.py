from bs4 import BeautifulSoup

from src.utils.constants import SUPPORTED_BATTLESCRIBE_VERSION


def check_battlescribe_version(roster):
    soup = BeautifulSoup(roster, features="lxml")
    battlescribe_version = soup.find("roster").attrs.get("battlescribeversion")
    if battlescribe_version >= SUPPORTED_BATTLESCRIBE_VERSION:
        return True
    return False
