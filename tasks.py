from celery import Celery
from kokoro_mlx import KokoroTTS
import threading

broker_url = 'amqp://shpeak1:password@127.0.0.1:5672/shpeak'
app = Celery('tasks', backend="rpc://", broker=broker_url)
stop_event = threading.Event()
tts = KokoroTTS.from_pretrained()

@app.task
def say(to_say):
    tts.speak(to_say, "af_nova", 1.5, True, stop_event, 24000)
