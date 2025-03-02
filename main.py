### CONFIG
TXT_MODE = False
# If it should just write the urls or if to put a 'start' infront of them to start them in your browser

FILE_TYPE = 'bat'
# Usual file types: 'sh', 'bat', 'txt'

GAME_NAME = 'cyberpunk2077'
# check nexusmods for the right spelling

DOWNLOAD_MODE = 'vortex'
# 'vortex': opens download page for vortex mod manager
# 'normal': opens download page for normal download (zip file)
# 'file': opens only the files tab
# 'none': doesn't open download page / opens the description page

### CODE
import json

with open('collection.json', 'r') as file:
    data = json.load(file)

mods = data["mods"]

with open(f'collection.{FILE_TYPE}', "w") as file:
    file.write('')

bat = open(f"collection.{FILE_TYPE}", "a")
for mods in mods:
    source = mods["source"]
    modId = source["modId"]
    fileId = source["fileId"]
    if not TXT_MODE: start = 'start '
    else: start = ''
    match DOWNLOAD_MODE:
        case 'vortex': download = f'?tab=files&file_id={fileId}&nmm=1'
        case 'normal': download = f'?tab=files&file_id={fileId}'
        case 'file': download = f'?tab=files'
        case 'none' | '': download = ''
        case _: raise IOError('No Download specified, reconfigurate to continue')
    url = f"{start}https://www.nexusmods.com/{GAME_NAME}/mods/{str(modId)}/{download}\n"
    bat.write(url)
    