import RPi.GPIO as gpio
import time
import loop
import pywhatkit

#loop
while True:
    loop.verify_password()

gpio.cleanup()