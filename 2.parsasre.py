import json
from pprint import pprint

with open("euro_2024.json") as file_handler:
    continut_parsat = json.load(file_handler)
    # print(type(continut_parsat), continut_parsat)


# print(continut_parsat.keys())


tara ="Romania"

# pprint(continut_parsat)

gropus = continut_parsat['groups']
# pprint(type(gropus))
pprint(gropus)
    
for gr in gropus:
    # print(type(gr))
    # pprint(gr['teams'])
    for team in gr['teams']:
        # print(type(team))
        # pprint(team)
        if team['name'] == tara:
            print(f'{tara} se afla in {gr['name']}')
            break