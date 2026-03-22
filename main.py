import psutil
import time
import os
from datetime import date
import shutil as s
import json
from pathlib import Path

def config_check():
    if os.path.isfile(Path("config.json")) == False:
        print('No config.json file detected.')
        select_folder()
    else:
        print('config.json loaded')
        return



def select_folder():
    print('Enter the file path for where your game saves are.')
    print('Should look like this - C:/Users/your_user/wherever_you_put_the_game_folder/LCEServerWindows64/Windows64/GameHDD/world/saveData.ms')
    game_folder = input('>>')
    print('Enter the file path for where your game saves are.')
    print('Should look like this - C:/Users/your_user/your_backup_folder/')
    backup_folder = input('>>')


    print(game_folder)
    print(backup_folder)

    config = {
        "game_save": game_folder,
        "backup_folder": backup_folder
    }

    out_path = Path("config.json")
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)



def load_json():
    with open("config.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
    print(json_data)

    game_folder = json_data["game_save"]
    backup_folder = json_data["backup_folder"]

    return game_folder, backup_folder


def initial_save(game_folder, backup_folder):
    original_file = game_folder
    copy_file = f'{backup_folder}/{date.today()}/{time.localtime()[3]}.{time.localtime()[4]}.ms'
    check_folder = f'{backup_folder}/{date.today()}/'

    for i in range(0, 1):

        if os.path.isdir(check_folder) == False:
            os.mkdir(check_folder)
        if os.path.isdir(check_folder) == True:
            s.copy(original_file, copy_file)
        if os.path.isfile(copy_file) == True:
            print(f'backup {time.localtime()[3]}.{time.localtime()[4]} was made.')
        if os.path.isfile(copy_file) == False:
            print(f'backup {time.localtime()[3]}.{time.localtime()[4]} FAILED!')


def backup(game_folder, backup_folder):

    original_file = game_folder
    copy_file = f'{backup_folder}/{date.today()}/{time.localtime()[3]}.{time.localtime()[4]}.ms'
    check_folder = f'{backup_folder}/{date.today()}/'

    if time.localtime()[4] == 0:

        if os.path.isdir(check_folder) == False:
            os.mkdir(check_folder)
        if os.path.isdir(check_folder) == True:
            s.copy(original_file, copy_file)
        if os.path.isfile(copy_file) == True:
            print(f'backup {time.localtime()[3]}.{time.localtime()[4]} was made.')
        if os.path.isfile(copy_file) == False:
            print(f'backup {time.localtime()[3]}.{time.localtime()[4]} FAILED!')



config_check()
load_json()
game_folder, backup_folder = load_json()
initial_save(game_folder, backup_folder)



while True:
    backup(game_folder, backup_folder)
