import RPi.GPIO as GPIO
import sys, time, random


GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)


n=1


def blue():
    GPIO.output(18,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(18, GPIO.LOW)
def green():
    GPIO.output(21,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(21, GPIO.LOW)
def red():
    GPIO.output(20,GPIO.HIGH)
    time.sleep(6)
    GPIO.output(20, GPIO.LOW)
def lightLoop(n):
    rando = random.randint(n-333, n+333)
    if n >= rando:
        print(rando)
        red()
        time.sleep(2)
        lightLoop(n)
    if n%2==0:
        print(f"blue{n}")
        n+=1
        blue()
        time.sleep(2)
        lightLoop(n)
    if n%3==0:
        green()
        print(f"green{n}")
        n+=1
        time.sleep(2)
        lightLoop(n)
    else:
        n+=1
        lightLoop(n)
        

    if KeyboardInterrupt:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18,GPIO.OUT)
        GPIO.output(18, GPIO.LOW)
        GPIO.setup(21,GPIO.OUT)
        GPIO.output(21, GPIO.LOW)
        GPIO.setup(20,GPIO.OUT)
        GPIO.output(20, GPIO.LOW)
        print('quitted')
        GPIO.cleanup()

        
lightLoop(n)

