#!/usr/bin/env python3

import paho.mqtt.publish as publish
from Messager import Messager

class MQTTClient(Messager):

    def __init__(self, hostname, username, password, topic="animon/identification"):
        self.hostname = hostname
        self.auth = {'username':username, 'password':password}
        self.topic = topic

    def send(self, msg):
        publish.single(self.topic, msg, hostname=self.hostname, auth=self.auth)