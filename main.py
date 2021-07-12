import loop
import os
if os.name == 'nt':
    from RPiSim.GPIO import GPIO as gpio
else:   
    import RPi.GPIO as gpio

#loop
while True:
    loop.verify_password()

gpio.cleanup()