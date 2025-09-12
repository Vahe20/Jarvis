from fuzzywuzzy import fuzz
from rus2num import Rus2Num
import asyncio

import core.speaker as speaker

import config.commands as executor
import config.executor as executor

r2n = Rus2Num()


async def handle_command(query: str):
    query = r2n(query)
    print(query)
    

    if fuzz.partial_ratio("неайти иконку", query) > 70:
        await executor.jarvis_screen(query)
        return

    best_match = None
    best_score = 0

    for command_name, triggers in executor.commands_dict['commands'].items():
        if isinstance(triggers, list):
            for trigger in triggers:
                score = fuzz.partial_ratio(trigger, query)
                if score > best_score:
                    best_score = score
                    best_match = command_name

    if best_score > 70:
        try:
            result, status = executor.executor(best_match, query)

            if result:
                speaker.speak_async(result)
                if status == "exit":
                    return "exit"
                elif status == "break":
                    return "break"
                elif status == "continue":
                    return "continue"
                else:
                    return "break"
            else:
                return "break"

        except Exception as e:
            speaker.speak_async("Произошла ошибка")
            print(e)
            return "break"




