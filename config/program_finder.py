import os
import shutil
import winreg

import config.commands as commands

CONFIG_FILE = "programs.json"

# --- ищем в реестре ---
def find_in_registry(exe_name: str):
    keys = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\App Paths"
    ]
    for reg_key in keys:
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_key)
            i = 0
            while True:
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    if exe_name.lower() in subkey_name.lower():
                        subkey = winreg.OpenKey(key, subkey_name)
                        value, _ = winreg.QueryValueEx(subkey, None)
                        return value
                    i += 1
                except OSError:
                    break
        except FileNotFoundError:
            continue
    return None

# --- ищем в PATH ---
def find_in_path(exe_name: str):
    return shutil.which(exe_name)

# --- ищем вручную в популярных папках ---
def search_common_dirs(exe_name: str):
    dirs_to_check = [
        os.environ.get("ProgramFiles", "C:\\Program Files"),
        os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)"),
        os.environ.get("LOCALAPPDATA", "C:\\Users\\%USERNAME%\\AppData\\Local"),
        "C:\\Windows\\System32"
    ]
    for base in dirs_to_check:
        for root, dirs, files in os.walk(base):
            if exe_name in files:
                return os.path.join(root, exe_name)
    return None

# --- универсальный поиск ---
def find_program(exe_name: str):
    return (
        find_in_registry(exe_name)
        or find_in_path(exe_name)
        or search_common_dirs(exe_name)
    )
    
    
def get_program_path(key: str, exe_name: str):
    settings = commands.load_settings()

    if key in settings["directories"]:
        if len(settings["directories"][key]) > 1:
            return settings["directories"][key]

    path = find_program(exe_name)
    if path:
        settings["directories"][key] = path
        commands.save_settings(settings)
        return path
    return None
