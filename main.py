import RPi.GPIO as gpio
import time
import loop

#loop
while True:
    loop.verify_password()

gpio.cleanup()