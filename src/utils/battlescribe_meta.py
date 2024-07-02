from bs4 import BeautifulSoup

from src.utils.constants import SUPPORTED_BATTLESCRIBE_VERSION


def check_battlescribe_version(roster):
    soup = BeautifulSoup(roster, features="xml")
    battlescribe_version = soup.find("roster").attrs.get("battleScribeVersion")
    return battlescribe_version >= SUPPORTED_BATTLESCRIBE_VERSION
