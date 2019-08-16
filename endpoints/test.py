import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
print "LED on"
GPIO.output(4,GPIO.HIGH)
time.sleep(7)
print "LED off"
GPIO.output(7,GPIO.LOW)