from gopigo import *
import time

class Pigo:

    isMoving = False
    servoPos = 90

    def __init__(self):
        print "I'm a little robot car. beep beep."

    def stop(self):
        self.isMoving = False
        while stop() != 1:
            time.sleep(.1)
            print "Yikes, looks like I can't stop!"

    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.sleep(.1)
            print "Sorry boss, can't seem to get moving."

tina = Pigo()
tina.fwd()
time.sleep(2)
tina.stop()
