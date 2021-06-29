#!/usr/bin/env python3

import paho.mqtt.publish as publish
from Message import Message

class MQTTClient(Message):

    def __init__(self, hostname, username, password, topic="animon/#"):
        self.hostname = hostname
        self.auth = {'username':username, 'password':password}
        self.topic = topic

    def send(self):
        publish.single(self.topic, "Oi, aqui é um teste", hostname=self.hostname)