import os
import threading
from elevenlabs import stream
from elevenlabs.client import ElevenLabs

import config
from gtts import gTTS
from playsound3 import playsound


elevenlabs = ElevenLabs(
    api_key='sk_817e138044d9225bd001c2fcbde26ef50514f36e70b92084',
)



def speak(text):
    try:
        playsound(config.sounds + "\\" + text + ".wav")
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
            os.remove(config.dirPath + "\\audio.wav")
        except:
            tts = gTTS(text=text, lang="ru", slow=False)
            tts.save(config.dirPath + "\\audio.mp3")
            playsound(config.dirPath + "\\audio.mp3")
            os.remove(config.dirPath + "\\audio.mp3")


def speak_async(text):
    threading.Thread(target=speak, args=(text,), daemon=True).start()