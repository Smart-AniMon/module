#!/usr/bin/env python3

from Sensor import Sensor
import Adafruit_DHT
import RPi.GPIO as GPIO

class HumidityTemperature(Sensor):

    def __init__(self, pino):

        self.sensor = Adafruit_DHT.DHT11  # outro tipo: Adafruit_DHT.DHT22
        self.pino_sensor = pino
        self.humidity = None
        self.temperature = None

    def get_value(self):
        '''Pegar a grandeza capturada pelo sensor'''

        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pino_sensor)
        if humidity is not None and temperature is not None:
            self.humidity = humidity
            self.temperature = temperature
        return humidity, temperature
    
    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity