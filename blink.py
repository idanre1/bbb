import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("USR0", GPIO.OUT)
GPIO.setup("USR1", GPIO.OUT)
GPIO.setup("USR2", GPIO.OUT)
GPIO.setup("USR3", GPIO.OUT)
GPIO.setup("P8_7", GPIO.OUT) # LED_RED
GPIO.setup("P8_8", GPIO.OUT) # LED_GRN

while True:
    GPIO.output("USR0", GPIO.HIGH)
    GPIO.output("USR1", GPIO.LOW)
    GPIO.output("USR2", GPIO.HIGH)
    GPIO.output("USR3", GPIO.LOW)
    GPIO.output("P8_7", GPIO.HIGH)
    GPIO.output("P8_8", GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output("USR0", GPIO.LOW)
    GPIO.output("USR1", GPIO.HIGH)
    GPIO.output("USR2", GPIO.LOW)
    GPIO.output("USR3", GPIO.HIGH)
    GPIO.output("P8_7", GPIO.LOW)
    GPIO.output("P8_8", GPIO.LOW)
    time.sleep(0.25)
