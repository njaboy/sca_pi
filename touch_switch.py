import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)

touch_pin = 31
led_pin = 11

GPIO.setup(touch_pin,GPIO.IN)
GPIO.setup(led_pin,GPIO.OUT)

while True:
        if GPIO.input(touch_pin) == 0 :
            GPIO.output (led_pin , False)
        if GPIO.input(touch_pin) ==1 :
            GPIO.output (led_pin , True)
            time.sleep(2)

# reset GPIO resources used by script
GPIO.cleanup ( )
