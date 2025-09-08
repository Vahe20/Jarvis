from vosk import KaldiRecognizer, Model
import pyaudio, json
import pvporcupine
import time

import config


vosk_model = Model(config.dirPath + "/core/vosk-model")
buffer = ["стиль", "код", "эпик"]

porcupine = pvporcupine.create(
    access_key=config.ACCESS_KEY,
    keywords=[].copy() + config.wake_word_update()
)

pa = pyaudio.PyAudio()
index = 0
stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    input_device_index=index,
    frames_per_buffer=porcupine.frame_length
)


def listen(phrase_time_limit=7):
    rec = KaldiRecognizer(vosk_model, 16000)
    rec.SetMaxAlternatives(10)
    start_time = time.time()

    while time.time() - start_time < phrase_time_limit:
        data = stream.read(4000, exception_on_overflow=False)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            return json.loads(rec.Result())

    return "error"
