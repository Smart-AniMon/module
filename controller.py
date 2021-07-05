#!/usr/bin/env python3

from threading import Timer

class Controller():

    def __init__(self, t_period):
        self.t = t_period
        self.timer = None
        self.count = 0

    def run(self):
        self.timer = Timer(self.t, self.identify)
        self.timer.start()

    def identify(self):
        print(str(self.count)+" - PHOTOGRAPH")
        self.count += 1
        self.run()


if __name__ == "__main__":
    controller = Controller(1)
    controller.run()
    print("Run")