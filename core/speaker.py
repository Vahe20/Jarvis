import os
import threading
from elevenlabs.client import ElevenLabs

import config.commands as commands
from gtts import gTTS
from playsound3 import playsound


settings = commands.load_settings()

elevenlabs = ElevenLabs(
    api_key=settings["API"]["eleven_API"]
)

def speak(text):
    try:
        playsound(commands.sounds + "\\" + text + ".wav")
    except:
        try:
            audio_stream = elevenlabs.text_to_speech.stream(
                text=text,
                voice_id="JBFqnCBsd6RMkjVDRZzb",
                model_id="eleven_multilingual_v2"
            )
            with open("audio.wav", "wb") as f:
                for chunk in audio_stream:
                    if isinstance(chunk, bytes):
                        f.write(chunk)

            playsound("audio.wav")
        except:
            tts = gTTS(text=text, lang="ru", slow=False)
            tts.save(commands.dirPath + "\\audio.mp3")
            playsound(commands.dirPath + "\\audio.mp3")
        finally:
            try:
                os.remove(commands.dirPath + "\\audio.wav")
            except FileNotFoundError:
                pass
            try:
                os.remove(commands.dirPath + "\\audio.mp3")
            except FileNotFoundError:
                pass


def speak_async(text):
    threading.Thread(target=speak, args=(text,), daemon=True).start()