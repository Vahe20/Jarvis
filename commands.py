import webbrowser
import os
import requests
import random
import datetime
import pyautogui
import re
from googletrans import Translator


import core.speaker as speaker
import config
import plagins.Timer as Timer
import plagins.openCv as openCv


def openYoutube():
    webbrowser.open("https://www.youtube.com/")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openYandex():
    webbrowser.open("https://yandex.ru/")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openSteam():
    os.startfile(config.steam())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openVsCode():
    os.startfile(config.vsCode())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openDiscord():
    os.startfile(config.discord())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openMinecraft():
    os.startfile(config.minecraft())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openEpicGames():
    os.startfile(config.epicGames())
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def gtaRp():
    os.startfile(config.gtaRp())
    return openEpicGames()

def openMyFolder():
    os.startfile("C:\\Users\\Karen Ghazaryan\\Desktop\\vahei papka\\programming")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def weather():
    url = "http://wttr.in/Yerevan?format=%t"
    weather = requests.get(url)
    return weather.text

def time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def screenShot():
    if not os.path.exists(config.dirPath + "/screenshots"):
        os.mkdir(config.dirPath + "/screenshots")
        
    name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = pyautogui.screenshot()
    screenshot.save(config.dirPath + "/screenshots/" + name + ".png")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def jarvis_timer(command):
    match = re.search(r'(\d+)\s*(минут|мин|секунд|сек)', command.lower())
    if not match:
        # print("Не удалось распознать время!")
        return

    number = int(match.group(1))
    unit = match.group(2)

    seconds = number * 60 if 'мин' in unit else number

    name_match = re.search(r'для (.+)', command.lower())
    name = name_match.group(1).capitalize() if name_match else "Таймер"

    message = f"Таймер '{name}' завершен!"

    timer = Timer.Timer(name, seconds, message)
    timer.start()
    
async def jarvis_screen(query):
    translator = Translator()
    screen = openCv.ScreenHelper()
    name_match = re.search(r"иконку (.+)", query)
    if not name_match:
        # print("Не удалось распознать имя!")
        return

    name = await translator.translate(name_match.group(1), src="ru", dest="en")

    try:
        screen.click_on_image(config.dirPath + "\\icons\\" + name.text.lower() + ".png")
    except:
        speaker.speak("Иконка не найдена")
    

def executor(funcName):
    return globals()[funcName]()