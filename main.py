from bs4 import BeautifulSoup

filename = "test.ros"
path_to_rosters = "./test_rosters/unzipped/"

with open(path_to_rosters + filename, "r") as roster:
    data = roster.read()

soup = BeautifulSoup(data, 'lxml')

game_system = soup.find("roster")
print(game_system.text)
