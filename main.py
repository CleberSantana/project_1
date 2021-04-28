import RPi.GPIO as gpio
import time
import teste

while True:
    teste.verify_password()

gpio.cleanup()