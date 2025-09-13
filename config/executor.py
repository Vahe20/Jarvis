import webbrowser
import os
import requests
import random
import datetime
import pyautogui
import re
import asyncio
import threading
import json
from googletrans import Translator

import core.speaker as speaker

import plagins.Ai as Ai
import plagins.Timer as Timer
import plagins.openCv as openCv
from plagins.psUtill import diagnose_pc
from plagins.jokes_plugin import get_joke

import config.commands as commands


def openYoutube(query=None):
    webbrowser.open("https://www.youtube.com/")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"]), "continue"

def openYandex(query=None):
    webbrowser.open("https://yandex.ru/")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"]), "continue"

def openSteam(query=None):
    os.startfile(commands.steam())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"]), "continue"

def openVsCode(query=None):
    os.startfile(commands.vsCode())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"]), "continue"

def openDiscord(query=None):
    os.startfile(commands.discord())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"]), "continue"

def openMinecraft(query=None):
    os.startfile(commands.minecraft())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"]), "continue"

def openEpicGames(query=None):
    os.startfile(commands.epicGames())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"]), "continue"

def openMyFolder(query=None):
    os.startfile("C:\\Users\\Karen Ghazaryan\\Desktop\\vahei papka\\programming")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"]), "continue"

def gtaRp(query=None):
    os.startfile(commands.gtaRp())
    return openEpicGames(), "continue"

def thanks(query=None):
    return "К вашим услугам сэр", "break"

def off(query=None):
    return "Отключаю питание", "exit"


def AI(query):
    try:
        asyncio.create_task(run_gpt(query))
        return "", "break"
    except Exception as e:
        return "Произошла ошибка", "break"
    
async def run_gpt(query: str):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, Ai.ask_gpt, query)
    speaker.speak_async(response)
    return

def weather(query=None):
    url = "http://wttr.in/Yerevan?format=%t"
    weather = requests.get(url)
    return weather.text, "break"

def time(query=None):
    return datetime.datetime.now().strftime("%H:%M:%S"), "break"

def diagnose(query=None):
    return diagnose_pc(), "break"

def anecdote(query=None):
    return get_joke(), "break"
    
def screenShot(query=None):
    if not os.path.exists(commands.dirPath + "/screenshots"):
        os.mkdir(commands.dirPath + "/screenshots")
        
    name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = pyautogui.screenshot()
    screenshot.save(commands.dirPath + "/screenshots/" + name + ".png")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"]), "continue"


def timer(query):
    threading.Thread(target=jarvis_timer, args=(query,)).start()
    return "Таймер запущен", "break"

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
    
def task(query):
    match = re.search(r"задачу (.+)", query.lower())
    if not match:
        return

    description = match.group(1)

    with open("tasks.json", "r", encoding="utf-8") as f:
        tasks = json.load(f)

    tasks.append({"description": description, "status": "в процессе"})

    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

    return "Задача добавлена", "break"
    
    
async def jarvis_screen(query):
    translator = Translator()
    screen = openCv.ScreenHelper()
    name_match = re.search(r"иконку (.+)", query)
    if not name_match:
        return

    name = await translator.translate(name_match.group(1), src="ru", dest="en")

    try:
        screen.click_on_image(commands.dirPath + "\\icons\\" + name.text.lower() + ".png")
    except:
        return "Иконка не найдена", "break"
    

def executor(funcName, query=None):
    return globals()[funcName](query)
