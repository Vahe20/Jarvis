import os
import threading

import config
from gtts import gTTS
from playsound3 import playsound

def speak(text):
    try:
        playsound(config.sounds + "\\" + text + ".wav")
    except:
        tts = gTTS(text=text, lang="ru", slow=False)
        tts.save(config.dirPath + "\\audio.mp3")
        playsound(config.dirPath + "\\audio.mp3")
        os.remove(config.dirPath + "\\audio.mp3")


def speak_async(text):
    threading.Thread(target=speak, args=(text,), daemon=True).start()