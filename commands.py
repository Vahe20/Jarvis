import webbrowser
import os
import requests
import random
import datetime
import pyautogui
import re
import asyncio
import threading
import plagins.Ai as Ai
from googletrans import Translator



import core.speaker as speaker

import plagins.Timer as Timer
import plagins.openCv as openCv
from plagins.psUtill import diagnose_pc
from plagins.jokes_plugin import get_joke

import config


def openYoutube(query=None):
    webbrowser.open("https://www.youtube.com/")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openYandex(query=None):
    webbrowser.open("https://yandex.ru/")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openSteam(query=None):
    os.startfile(config.steam())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openVsCode(query=None):
    os.startfile(config.vsCode())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openDiscord(query=None):
    os.startfile(config.discord())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openMinecraft(query=None):
    os.startfile(config.minecraft())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openEpicGames(query=None):
    os.startfile(config.epicGames())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def thanks(query=None):
    return "К вашим услугам сэр"

def off(query=None):
    return "Отключаю питание"

def gtaRp(query=None):
    os.startfile(config.gtaRp())
    return openEpicGames()

def AI(query):
    try:
        asyncio.create_task(run_gpt(query))
    except Exception as e:
        speaker.speak_async("Произошла ошибка")
        return
    
async def run_gpt(query: str):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, Ai.ask_gpt, query)
    speaker.speak_async(response)
    return
def weather(query=None):
    url = "http://wttr.in/Yerevan?format=%t"
    weather = requests.get(url)
    return weather.text

def time(query=None):
    return datetime.datetime.now().strftime("%H:%M:%S")

def diagnose(query=None):
    
    return diagnose_pc() 

def anecdote(query=None):
    return get_joke()
    
def screenShot(query=None):
    if not os.path.exists(config.dirPath + "/screenshots"):
        os.mkdir(config.dirPath + "/screenshots")
        
    name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = pyautogui.screenshot()
    screenshot.save(config.dirPath + "/screenshots/" + name + ".png")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])


def timer(query):
    threading.Thread(target=jarvis_timer, args=(query,)).start()
    return

def jarvis_timer(query):
    match = re.search(r'(\d+)\s*(минут|мин|секунд|сек)', query.lower())
    if not match:
        return

    number = int(match.group(1))
    unit = match.group(2)

    seconds = number * 60 if 'мин' in unit else number

    name_match = re.search(r'для (.+)', query.lower())
    name = name_match.group(1).capitalize() if name_match else "Таймер"

    message = f"Таймер '{name}' завершен!"

    timer = Timer.Timer(name, seconds, message)
    timer.start()
    
    
async def jarvis_screen(query):
    translator = Translator()
    screen = openCv.ScreenHelper()
    name_match = re.search(r"иконку (.+)", query)
    if not name_match:
        return

    name = await translator.translate(name_match.group(1), src="ru", dest="en")

    try:
        screen.click_on_image(config.dirPath + "\\icons\\" + name.text.lower() + ".png")
    except:
        speaker.speak("Иконка не найдена")
    

def executor(funcName, query=None):
    return globals()[funcName](query)

