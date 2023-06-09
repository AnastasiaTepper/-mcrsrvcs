import os

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/data")


def on_message(client, userdata, msg):
    print(msg.payload.decode())


client = mqtt.Client()
client.connect(os.environ.get("MQTT_HOST", "localhost"), os.environ.get("MQTT_PORT", 1883))
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
