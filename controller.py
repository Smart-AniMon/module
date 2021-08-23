#!/usr/bin/env python3

from MQTTClient import MQTTClient
from threading import Timer
from Camera import Camera
from HumidityTemperature import HumidityTemperature
import RPi.GPIO as GPIO
import json, base64, datetime, signal, sys, argparse

DEBUG = False
CAM_ID = 0
PIR_GPIO = 23
JSON_MSG = '{"id":"testID","image":"testIMAGE","temperature":"testTEMPER","humidity":"testHUMID","localization":{"latitude":"testLAT","longitude":"testLONG"},"capture_date":"testDATE"}'

# Colors
RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RST = '\033[0;0m'

class Controller():

    def __init__(self, id_camera, messenger, images_directory):
        self.count = 0
        self.id_camera = id_camera
        self.messenger = messenger
        self.images_directory = images_directory
        self.humidity_temperature = HumidityTemperature(24)
    
    def convert_image_base64(self, path):
        image = open(path,'rb')
        image_bytes = image.read()
        image_base64 = base64.b64encode(image_bytes)
        return image_base64
    
    def build_message(self, image_base64, humidity, temperature):
        parsed_json = json.loads(JSON_MSG)
        parsed_json['id'] = str(self.count)
        parsed_json['image'] = image_base64.decode('utf-8')
        parsed_json['humidity'] = str(humidity)
        parsed_json['temperature'] = str(temperature)
        parsed_json['capture_date'] = str(datetime.datetime.now())
        string_json = json.dumps(parsed_json)
        return string_json

    def photo_capture(self, image_path):
        was_captured = Camera.get_value(self.id_camera, image_path)
        return was_captured

    def environment_capture(self):
        humidity, temperature = self.humidity_temperature.get_value() 
        if humidity is None or temperature is None:
            debug("ERROR : Failed to capture humidity and temperature", YELLOW)
            humidity = self.humidity_temperature.get_last_humidity()
            temperature = self.humidity_temperature.get_last_temperature()
        debug("Humidity: "+str(humidity)+"    Temperature: "+str(temperature))
        return humidity, temperature

    def identify(self, value):

        debug("IDENTIFY!", BLUE)
        image_path  =self.images_directory+str(self.count)+".png"
        was_captured = self.photo_capture(image_path)
        
        if was_captured:
            debug("Photograph")            
            humidity, temperature = self.environment_capture()
            image_base64 = self.convert_image_base64(image_path)
            message = self.build_message(image_base64, humidity, temperature)
            self.messenger.send(message)
            debug("Message sent", GREEN)
            self.count += 1
        
        else: debug("ERROR: Failed to capture image", RED)


def get_credentials():
    ref_arquivo = open("credentials.txt","r")
    credentials = ref_arquivo.readlines()
    username = credentials[0].rstrip('\n')
    password = credentials[1].rstrip('\n')
    hostname = credentials[2].rstrip('\n')
    topic = credentials[3].rstrip('\n')
    return username, password, hostname, topic

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def debug(msg, code=""):
    if DEBUG: 
        if code == RED:      sep = " X "
        elif code == YELLOW: sep = " ! "
        else :               sep = " - "
        print(str(datetime.datetime.now())+code+sep+msg+RST)

if __name__ == "__main__":
    
    # Visualização de ajuda
    parser = argparse.ArgumentParser(description='Smart AniMon Module')
    parser.add_argument('-D','--debug', help='enable debugging', action='store_true', dest='debug')
    args = parser.parse_args()
    DEBUG = args.debug
    
    debug("Debugging enabled", BLUE)

    username, password, hostname, topic = get_credentials()
    mqtt = MQTTClient(hostname, username, password, topic)
    controller = Controller(CAM_ID, mqtt, "./images/image")
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_GPIO, GPIO.IN)
    GPIO.add_event_detect(PIR_GPIO, GPIO.RISING, callback=controller.identify, bouncetime=100)
    
    debug("Run\n\n", GREEN)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()