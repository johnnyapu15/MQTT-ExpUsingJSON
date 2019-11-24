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
def exp(filename, expName = "test", velo = 0):
    filename = './Jsons/' + filename + '.json'
    sceneFile = open(filename, 'r')
    scene = json.load(sceneFile)
    t = 0
    for i, e in enumerate(scene['data']):
        print(e)
        if (e[topic] == 'Fire'):
            e[d]['messageId'] = expName
        if (e[topic] == 'Test-mW'):
            e[d]['value2'] = velo
        if t >= e[ts]:
            # play
            mqttc.publish(e[topic], str(e[d]))
        else:
            time.sleep(e[ts] - t)
            # play
            mqttc.publish(e[topic], str(e[d]))
        t = e[ts]
def exp2(test):
    global mqttc
    mqttc = mqtt.Client()
    mqttc.connect(brok, port)
    #kin-A-2
    testVelo = 4.2 # 4.2m/s ~= 15km/h
    d = test.split('-')
    building = d[0]
    exp(building + '-init',None,testVelo)
    statName = d[0]
    for i, e in enumerate(d[1:]):
        exp(building + '-' + e,None,testVelo)
        statName += '-' + e
    exp('Fire', statName)
#exp2('kin-A-1')