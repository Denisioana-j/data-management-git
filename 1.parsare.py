import json

# link = 'https://dontpad.com/euro2024'
# versiunea1
with open("euro_2024.json") as file_handler:
    # citesc continutul
    continut = file_handler.read()
    print(type(continut), continut)
    # parsare continut
    continut_parsat = json.loads(continut)
    print(type(continut_parsat), continut_parsat)

# versiunea2: citire+parsare(direct)
with open("euro_2024.json") as file_handler:
    continut_parsat = json.load(file_handler)
    print(type(continut_parsat), continut_parsat)



