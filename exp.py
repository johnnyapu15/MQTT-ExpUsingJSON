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
        if (e[topic] == 'Test-Target'):
            e[d]['value'] = velo
        if t >= e[ts]:
            # play
            mqttc.publish(e[topic], str(e[d]))
        else:
            time.sleep(e[ts] - t)
            # play
            mqttc.publish(e[topic], str(e[d]))
        t = e[ts]
def exp2(test, sub = None):
    global mqttc
    mqttc = mqtt.Client()
    mqttc.connect(brok, port)
    #kin-A-2
    # 19km/h = 5.3m/s

    testVelo = 5.3 # 4.2m/s ~= 15km/h
    d = test.split('-')
    building = d[0]
    exp(building + '-init',None,testVelo)
    statName = d[0]
    for i, e in enumerate(d[1:]):
        exp(building + '-' + e,None,testVelo)
        statName += '-' + e
    if sub != None:
        statName += sub
    exp('Fire', statName)

def t(f):
    global mqttc
    mqttc = mqtt.Client()
    mqttc.connect(brok, port)
    exp('settarget',None, f)
#exp2('kin-A-1')



# t(1)
# exp2('etri-A-1','first')
# input()
# exp2('etri-A-2','first')
# input()
# exp2('etri-A-3','first')
# input()
# exp2('etri-B-1','first')
# input()
# exp2('etri-B-2','first')
# input()
# exp2('etri-B-3','first')
# input()
# t(6)
# exp2('etri-A-1','last')
# input()
# exp2('etri-A-2','last')
# input()
# exp2('etri-A-3','last')
# input()
# exp2('etri-B-1','last')
# input()
# exp2('etri-B-2','last')
# input()
# exp2('etri-B-3','last')
# input()