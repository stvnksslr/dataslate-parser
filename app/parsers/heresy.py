from bs4 import BeautifulSoup


def parse_units(contents):
    soup = BeautifulSoup(contents, "lxml")
    unit_list = soup.findAll("selection", {"type": "unit"})
    parsed_unit_list = [unit_list]
    return parsed_unit_list
