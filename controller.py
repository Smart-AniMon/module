#!/usr/bin/env python3

from threading import Timer
from Camera import Camera

class Controller():

    def __init__(self, t_period, id_camera):
        self.t = t_period
        self.timer = None
        self.count = 0
        self.id_camera = id_camera

    def run(self):
        self.timer = Timer(self.t, self.identify)
        self.timer.start()

    def identify(self):
        caminho = Camera.get_value(self.id_camera, "./images/image"+str(self.count)+".png")
        print(str(self.count)+" - PHOTOGRAPH: "+caminho)
        self.count += 1
        self.run()


if __name__ == "__main__":
    controller = Controller(1, 0) # t_period (mudar para 60 segundos), id_camera (0: camNotebook, 2: camUSB)
    controller.run()
    print("Run")