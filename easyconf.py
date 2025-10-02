### PRE-STUFF
import json
import os
from typing import Callable
def clearConsole(): os.system('cls' if os.name=='nt' else 'clear')

### CONFIG
def restart_section(function: Callable, choice: str, avail_choices: str, use_print: bool):
    if use_print == True:
        clearConsole()
        print(f"Error: available choices: {avail_choices}; you said {choice}")
    function()
def conf():
    clearConsole()
    def txt():
        global TXT_MODE
        txt_choice = input("Do you want the generated file to be instantly runnable (uses the 'start' command to open all mods in browser) [Y/n] ")
        match txt_choice.lower():
            case "": TXT_MODE = True
            case "y": TXT_MODE = True
            case "n": TXT_MODE = False
            case _: restart_section(txt, txt_choice.lower, "y/n", use_print=True)
    def filetype():
        global FILE_TYPE
        ft_choice = input("What filetype should the generated file be? [recommended: bat (windows, default), sh (linux, mac)] ")
        if ft_choice == "json": restart_section(filetype, ft_choice, "anything except json", True)
        elif ft_choice == "": ft_choice = "bat"
        else: FILE_TYPE = ft_choice
    def download():
        global DOWNLOAD_MODE
        print("How should the mods be downloaded?\nvortex: opens the download page for the vortex mod manager\nnormal: opens the download page for the normal file\nfile: opens the file tab of the mod\nnone: opens the description tab of the mod")
        dl_choice = input("[vortex (default), normal, file, none] ")
        if dl_choice == "": dl_choice = "vortex"
        DOWNLOAD_MODE = dl_choice
    txt()
    filetype()
    download()

### CODE
conf()
with open('collection.json', 'r') as file:
    data = json.load(file)

mods = data["mods"]
info = data["info"]
game = info["domainName"]
GAME_NAME = game

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
    