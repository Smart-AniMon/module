#!/usr/bin/env python3

from MQTTClient import MQTTClient
from threading import Timer
from Camera import Camera
import json

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

    def identify(self):
        caminho = Camera.get_value(self.id_camera, "./images/image"+str(self.count)+".png")
        print(str(self.count)+" - PHOTOGRAPH: "+caminho)
        
        # 1. transformar imagem em bytes


        # 2. adicionar num objeto json
        parsed_json = json.loads(json_msg)
        parsed_json['id'] = str(self.count)
        
        
        # 3. enviar para o broker
        self.messenger.send(json.dumps(parsed_json))
        

        self.count += 1
        self.run()

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

    controller = Controller(1, 0, mqtt) # t_period (mudar para 60 segundos), id_camera (0: camNotebook, 2: camUSB)
    
    controller.run()
    print("Run")