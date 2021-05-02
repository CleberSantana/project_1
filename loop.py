import RPi.GPIO as gpio
import time
import json
import data_exchange
import pywhatkit

#setting GPIO
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)

#reading passwords
file = open('password.txt', 'r')
password = file.readline().strip()
safe_password = file.readline().strip()
change_password = file.readline().strip()
#print(password,safe_password,change_password)

#define new password
def new_password():
    new_pass = input ("Insert new password")
    file = open('password.txt', 'r')
    password = file.readline().strip()
    safe_password = file.readline().strip()
    change_password = file.readline().strip()
    file.close()
    #writing new password
    file = open('password.txt', 'w')
    wpass = new_pass
    file.write(wpass + '\n')
    file.write(safe_password + '\n')
    file.write(change_password)
    file.close()
       
def verify_password():
    waiting = input()
    #waiting "s" key
    if waiting == "s":
        file = open('password.txt', 'r')
        password = file.readline().strip()
        safe_password = file.readline().strip()
        change_password = file.readline().strip()
        file.close()
        print(password,safe_password,change_password)
        a = input ("Insert password:")
        if a == "c":
            return
        if a == password:
            gpio.output(17,gpio.HIGH)
            time.sleep(1)
            gpio.output(17,gpio.LOW)
            print("Password")
            data_exchange.msg('user1', password, pass_type = "Password")
            pywhatkit.sendwhatmsg('+5541988248333', 'test', 6, 6)
            return
        if a == safe_password:
            gpio.output(17,gpio.HIGH)
            time.sleep(1)
            gpio.output(17,gpio.LOW)
            print("Safe_Password")
            data_exchange.msg('user1', safe_password, pass_type = "Safe_password")
            return
        if a == change_password:
            new_password()
            print("Change_Password")
            return
        else:
            print("Wrong password")