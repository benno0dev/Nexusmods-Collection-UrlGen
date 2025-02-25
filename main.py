### CONFIG
TXT_MODE = False # If it should just write the urls or if to put a 'start' infront of them to start them in your browser
FILE_TYPE = 'bat' # Usual file types: 'sh', 'bat', 'txt'
GAME_NAME = 'cyberpunk2077' # check nexusmods for the right spelling

### CODE
import json

with open('collection.json', 'r') as file:
    data = json.load(file)

mods = data["mods"]

bat = open(f"collection.{FILE_TYPE}", "a")
for mods in mods:
    source = mods["source"]
    modId = source["modId"]
    if not TXT_MODE:
        url = "start " + f"https://www.nexusmods.com/{GAME_NAME}/mods/" + str(modId) + "/?tab=files\n"
    else:
        url = f"https://www.nexusmods.com/{GAME_NAME}/mods/" + str(modId) + "/?tab=files\n"
    bat.write(url)
    