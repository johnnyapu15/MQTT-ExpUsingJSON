import paho.mqtt.client as mqtt
import json
import time

brok = "mqtt-dashboard.com"
port = 1883

# Keys
ts = 'timestamp'
topic = 'Topic'
d = 'data'
aId = 'areaId'
v = 'value'
v2 = 'value2'



mqttc = mqtt.Client()
mqttc.connect(brok, port)
def exp(filename):
    filename = './Jsons/test.json'
    sceneFile = open(filename, 'r')
    scene = json.load(sceneFile)
    t = 0
    for i, e in enumerate(scene['data']):
        print(e)
        if t >= e[ts]:
            # play
            mqttc.publish(e[topic], str(e[d]))
        else:
            time.sleep(e[ts] - t)
            # play
            mqttc.publish(e[topic], str(e[d]))
        t = e[ts]
