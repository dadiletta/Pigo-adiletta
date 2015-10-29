from gopigo import *
import time

__author__ = 'adilettad'

class Pigo:

    isMoving = False

    def __init__(self):
        print "I'm a little robot car! Beep beep."

    def stop(self):
        self.isMoving = False
        while stop() != 1:
            time.sleep(.1)
            print "Eek! I'm having trouble stopping."



tina = Pigo()
tina.stop()