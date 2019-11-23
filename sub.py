import paho.mqtt.client as mqtt


brok = "13.124.77.110"
port = 1883
topics = ['nodemcu', 'Request']


def on_connect(cli, userdata, rc):
    print("Connecting..." + str(rc))
    for i, topic in enumerate(topics):
        client.subscribe(topic)

def on_message(cli, userdata, msg):
    print("Topic: " + msg.topic + " | Msg: " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(brok, port, 60)

client.loop_forever()