# Nexusmods Collection Url Generator
A python script that creates you a url list of all mods in a nexusmods mod collection

# Installation
- Install Python
- Clone the repository or just download main.py
- Finished 🥳

# How to use?
At first, configurate the script (see [Config](https://github.com/benno0dev/Nexusmods-Collection-UrlGen/#Config)).
I assume you already downloaded the pack or at least added it, so a collection.json was created at ```C:\Users\<username>\AppData\Roaming\Vortex\<game>\<collection+some numbers>\collection.json``` but check ```vortex > settings > mods``` for that.
Now copy the collection.json to the folder the main.py is in and execute the script.
Now a collection.txt or what ever you put as your file type was created.
Thats all, have fun!

# Config
TXT_MODE:
- True: just writes the urls in seperate lines
- False: writes a "start" in front of every url, so it automatically opens every url in your default browser

FILE_TYPE:
> technically all files types are supported, these are just the ones i recommend
  - txt
  - sh
  - bat

GAME_NAME:
- Enter the name of the game that is used in the nexusmods url (e.g. "cyberpunk2077")
