import os
import json
from pathlib import Path

#Available default keywords are:\n  hey google, hey siri, pico clock, americano, 
#hey barista, computer, grapefruit, grasshopper, jarvis, terminator, picovoice, bumblebee, porcupine, alexa, blueberry, ok google
START_WORD = ["jarvis"]
ACCESS_KEY = "3rXSA8EZIAa9DqGoomCvvqVBdQkGAKZt7lIPOTTmauMMPSn7K11uuA=="    
        

dirPath = os.path.dirname(os.path.realpath(__file__))
sounds = dirPath + "\\sounds"

commands_dict = {
    'commands': {
        'openYoutube': ['ютуб'],
        'openYandex': ['яндекс'],
        'openSteam': ["steam", 'стим', 'игры', 'тим', 'стиль'],
        'openVsCode': ['код', 'вс код'],
        'openEpicGames': ["epic games", "эпик гамес", "эпик геймс"],
        'gtaRp': ["гта рп", "гтарп", "гта 5 рп", "гта5рп"],
        'weather': ['погода'],
        'time': ['время', "Сколько времени"],
        'openDiscord': ['дискорд', "дискорт", "дискор", "эскорд"],
        'openMinecraft': ["майнкрафт"],
        'screenShot': ['скриншот'],
        'thanks': ['спасибо'],
        'off': ['отключись'],
        'AI': ['скажи'],
        'timer': ['таймер'],
        'diagnose': ['диагностика'],
        'anecdote': ['анекдот'],
    }
}


CONFIG_FILE = Path("settings.json")

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
    return load_settings().get("steam")

def discord():
    return load_settings().get("discord")

def vsCode():
    return load_settings().get("vsCode")

def minecraft():
    return load_settings().get("minecraft")

def epicGames():
    return load_settings().get("epicGames")

def gtaRp():
    return load_settings().get("gtaRp")


