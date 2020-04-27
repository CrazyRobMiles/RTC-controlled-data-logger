from umqtt.robust import MQTTClient
import time

class mqttstore():

    def __init__(self, host, devnanme, username, password, topic):
        self.host = host
        self.username = username
        self.password = password
        self.topic = topic
        self.client = MQTTClient(client_id=devname,server=host,user=username,password=password, keepalive=4000)
        self.connected = False

    def blocking_connect(self, timout_secs=5):
        self.connect()
        self.connected = True
        return self.connected

    def send_data(self, message):
        self.client.publish(self.topic, message)

    def disconnect(self):
        self.client.disconnect()
        
