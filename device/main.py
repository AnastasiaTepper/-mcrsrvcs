import logging
import os

import paho.mqtt.client as paho
import time
import random
logging.basicConfig(level=logging.NOTSET, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)s - %(funcName)20s() ]  ")

device = os.environ.get("DEVICE_NAME", "moshe")
client = paho.Client("admin")
client.connect(os.environ.get("MQTT_HOST", "localhost"), os.environ.get("MQTT_PORT", 1883))

while True:
    d = random.randint(1, 5)
    message = f"Device: {device}. Message: {d}"
    time.sleep(d)
    ret = client.publish("/data", message)
    logging.debug(message)
