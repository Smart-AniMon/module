#!/usr/bin/env python3

from MQTTClient import MQTTClient
from threading import Timer
from Camera import Camera
import json
import base64
import datetime

# texto = '{"atributo1": "valor 1", "atributo2": 23}'
# objeto = json.loads(texto)
# print(objeto['atributo1'])

json_msg = '{"id":"testID","image":"testIMAGE","temperature":"testTEMPER","humidity":"testHUMID","localization":{"latitude":"testLAT","longitude":"testLONG"},"capture_date":"testDATE"}'

class Controller():

    def __init__(self, t_period, id_camera, messenger):
        self.t = t_period
        self.timer = None
        self.count = 0
        self.id_camera = id_camera
        self.messenger = messenger

    def run(self):
        self.timer = Timer(self.t, self.identify)
        self.timer.start()
    
    def convert_image_base64(self, path):
        image = open(path,'rb')
        image_bytes = image.read()
        image_base64 = base64.b64encode(image_bytes)
        return image_base64
    
    def build_message(self, image_base64):
        parsed_json = json.loads(json_msg)
        parsed_json['id'] = str(self.count)
        parsed_json['image'] = image_base64.decode('utf-8')
        parsed_json['capture_date'] = str(datetime.datetime.now())
        string_json = json.dumps(parsed_json)
        return string_json

    def identify(self):

        image_path  ="./images/image"+str(self.count)+".png"
        is_captured = Camera.get_value(self.id_camera, image_path)
        
        if is_captured:
            print(str(self.count)+" - PHOTOGRAPH")
            
            image_base64 = self.convert_image_base64(image_path)
            message = self.build_message(image_base64)
            self.messenger.send(message)

            self.count += 1
            self.run()
        else:
            print("STOP: Image capture failed")

def get_credentials():
    ref_arquivo = open("credentials.txt","r") 
    return ref_arquivo.readlines()

if __name__ == "__main__":
    
    credentials = get_credentials()

    username = credentials[0].rstrip('\n')
    password = credentials[1].rstrip('\n')
    hostname = credentials[2].rstrip('\n')
    topic = credentials[3].rstrip('\n')
    
    mqtt = MQTTClient(hostname, username, password, topic)

    controller = Controller(5, 0, mqtt) # t_period (mudar para 60 segundos), id_camera (0: camNotebook, 2: camUSB)
    
    controller.run()
    print("Run")