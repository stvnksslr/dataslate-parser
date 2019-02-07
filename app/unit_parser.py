from bs4 import BeautifulSoup


class UnitParser:
    @staticmethod
    def parse_units(contents):
        soup = BeautifulSoup(contents, "html")
        unit_list = soup.findAll("selection", {"type": "model"})
        for unit in unit_list:
            pass
        return unit_list
