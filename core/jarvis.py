from fuzzywuzzy import fuzz
from rus2num import Rus2Num

import core.speaker as speaker

import config
import commands

r2n = Rus2Num()


async def handle_command(query: str):
    query = r2n(query)

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
            result = commands.executor(best_match, query)
            if result:
                speaker.speak_async(result)
                if (result == "Отключаю питание"):
                    return "exit"
                elif (result == "К вашим услугам сэр"):
                    return "thanks"
                return "break"
            else:
                return "break"
        except Exception as e:
            # speaker.speak_async("Произошла ошибка")
            print(e)
            return "break"



