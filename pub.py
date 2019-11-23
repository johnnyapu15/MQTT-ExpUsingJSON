import paho.mqtt.client as mqtt

brok = "13.124.77.110"
port = 1883
topic = 'nodemcu'

mqttc = mqtt.Client()

mqttc.connect(brok, port)

mqttc.publish(topic, "test msg...")

mqttc.loop(2)

print("test.")