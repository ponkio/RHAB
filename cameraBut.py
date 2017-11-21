#!/usr/bin/python

from sense_hat import SenseHat
import RPi.GPIO as GPIO
from time import sleep

##SenseHat var
sense = SenseHat()
sense.set_rotation(270)

##GPIO inputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)


##GPIO actions
try:
        while True:
                if GPIO.input(19) == False:
                        print "Camera Button"
                        sense.show_message("Camera running")
                        execfile("/home/pi/RHAB/cameraIGuess.py")
                        sleep(0.3)

finally:
        GPIO.cleanup()


