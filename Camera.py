#!/usr/bin/env python3

from logging import exception
from types import TracebackType
from Sensor import Sensor
import cv2
import imutils
import time

class Camera(Sensor):

    def get_value(id, path):
        '''Pegar a grandeza capturada pelo sensor'''

        cap = cv2.VideoCapture(id)
        (grabbed, frame) = cap.read()
        if grabbed:
            showimg = frame
            cv2.imwrite(path, frame)
            cap.release()
        
        return grabbed