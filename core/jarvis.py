from fuzzywuzzy import fuzz
from rus2num import Rus2Num
import threading
import asyncio

import core.recognizer as recognizer
import core.speaker as speaker

import plagins.gAi as gAi

import config
import commands


r2n = Rus2Num()


async def handle_command(query: str):
    if query in ["отключись"]:
        speaker.speak("Отключаю питание")
        return "exit"

    if query in ["спасибо"]:
        speaker.speak_async("К вашим услугам сэр")
        return

    if "скажи" in query:
        speaker.speak_async("Да сэр")
        query = await recognizer.listen()
        asyncio.create_task(run_gpt(query))
        return

    if fuzz.partial_ratio("запусти таймер", query) > 70:
        seconds = r2n(query)
        threading.Thread(target=commands.jarvis_timer, args=(seconds,)).start()
        return

    if fuzz.partial_ratio("неайти иконку", query) > 70:
        await commands.jarvis_screen(query)
        return

    best_match = None
    best_score = 0

    for command_name, triggers in config.commands_dict['commands'].items():
        if isinstance(triggers, list):
            for trigger in triggers:
                score = fuzz.partial_ratio(trigger, query)
                if score > best_score:
                    best_score = score
                    best_match = command_name

    if best_score > 70:
        try:
            result = commands.executor(best_match)
            if result:
                speaker.speak_async(result)
                return "break"
        except Exception as e:
            speaker.speak_async("Произошла ошибка")
            return "break"


async def run_gpt(query: str):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, gAi.ask_gpt, query)
    speaker.speak_async(response)
