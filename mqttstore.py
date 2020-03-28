

import paho.mqtt.client as mqtt 
import time



class mqttstore():

    def __init__(self, host, devnanme, username, password, topic):
        self.host = host
        self.username = username
        self.password = password
        self.topic = topic
        self.client = mqtt.Client(devnanme)
        self.client.on_connect=self.on_connect
        self.client.username_pw_set(username=username,password=password)
        self.connected = False

    def blocking_connect(self, timout_secs=5):

        if self.connected:
            return True

        self.client.connect(self.host)
        

        sec_count = 0
        while (sec_count < timout_secs) & (not self.connected):
            self.client.loop()
            time.sleep(1)

        return self.connected

    def on_connect(self, client, userdata, flags, rc):
        if rc==0:
            self.connected = True

    def send_data(self, message):
        self.client.publish(self.topic, message)

    def disconnect(self):
        self.client.disconnect()
        
