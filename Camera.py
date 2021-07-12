#!/usr/bin/env python3

from Sensor import Sensor
import cv2
import imutils
import time

class Camera(Sensor):

    def get_value(id, path):
        '''Pegar a grandeza capturada pelo sensor'''
        cap = cv2.VideoCapture(id) # id=2 para camera USB / id=0 para camera do note
        # ret, frame = self.cap.read()
        (grabbed, frame) = cap.read()
        showimg = frame
        # cv2.imshow('img1', showimg)  # display the captured image
        # cv2.waitKey(1)
        time.sleep(0.3) # Wait 300 miliseconds
        cv2.imwrite(path, frame)
        cap.release()
        return path                                                        ## retorna o caminho da imagem, precisa retornar bytes