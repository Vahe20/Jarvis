import json
from pathlib import Path

import config.program_finder as program_finder

#Available default keywords are:\n  hey google, hey siri, pico clock, americano, 
#hey barista, computer, grapefruit, grasshopper, jarvis, terminator, picovoice, bumblebee, porcupine, alexa, blueberry, ok google
START_WORD = ["jarvis"]
ACCESS_KEY = "3rXSA8EZIAa9DqGoomCvvqVBdQkGAKZt7lIPOTTmauMMPSn7K11uuA=="    
        

dirPath = str(Path(__file__).resolve().parent.parent)
sounds = dirPath + "\\sounds"

commands_dict = {
    'commands': {
        'openYoutube': ['ютуб'],
        'openYandex': ['яндекс'],
        'openSteam': ["steam", 'стим', 'игры', 'тим', 'стиль'],
        'openVsCode': ['код', 'вс код'],
        'openEpicGames': ["epic games", "эпик гамес", "эпик геймс"],
        'gtaRp': ["гта", "гта 5", "гта 5", "когда 5", "это 5"],
        'weather': ['погода'],
        'time': ['время', "Сколько времени"],
        'openDiscord': ['дискорд', "дискорт", "дискор", "эскорд"],
        'openMinecraft': ["майнкрафт"],
        'screenShot': ['скриншот'],
        'openMyFolder': ['открой мою папку'],
        'thanks': ['спасибо', "я не стобой"],
        'off': ['отключись'],
        'anecdote': ['анекдот'],
        'AI': ['скажи', "найди"],
        'timer': ['таймер'],
        "task": ['задачу'],
        'diagnose': ['диагностика'],
    }
}

CONFIG_FILE = Path(dirPath + "/config/settings.json")

def load_settings():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_settings(settings: dict):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4, ensure_ascii=False)
        
    wake_word_update()

                
def wake_word_update():
    settings = load_settings()
    wake_words = settings.get("wake word", {"jarvis": "True"})

    for word, value in wake_words.items():
        if str(value).lower() == "true":
            if word not in START_WORD:
                START_WORD.append(word)
        else:
            if word in START_WORD:
                START_WORD.remove(word)

    return START_WORD

def steam():
    return program_finder.get_program_path("steam", "steam.exe")

def discord():
    return program_finder.get_program_path("discord", "Update.exe")

def vsCode():
    return program_finder.get_program_path("vsCode", "Code.exe")

def minecraft():
    return program_finder.get_program_path("minecraft", "TLauncher.exe")

def epicGames():
    return program_finder.get_program_path("epicGames", "EpicGamesLauncher.exe")

def gtaRp():
    return program_finder.get_program_path("gtaRp", "GTA5.exe")