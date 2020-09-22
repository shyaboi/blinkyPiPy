import RPi.GPIO as GPIO
import sys
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
n=1


def blue():
    GPIO.output(18,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(18, GPIO.LOW)
def green():
    GPIO.output(21,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(21, GPIO.LOW)
def lightLoop(n):
    if n%2==0:
        n+=1
        print(n)
        blue()
        time.sleep(2)
        lightLoop(n)
    if n%3==0:
        green()
        time.sleep(2)
        lightLoop(n)
    else:
        lightLoop(n)
        n+=1

    if KeyboardInterrupt:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18,GPIO.OUT)
        GPIO.output(18, GPIO.LOW)
        GPIO.setup(21,GPIO.OUT)
        GPIO.output(21, GPIO.LOW)
        print('quitted')
        GPIO.cleanup()

        
lightLoop(n)

