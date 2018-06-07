import random

import RPi.GPIO as GPIO
import time

i = 0
random_number = random.randint(1,10)

while i < 10:
    i = i + 1
    guess = int(raw_input("Guess a number from 1 to 10: "))
    if guess < random_number:
        print 'Guess is to low'
        GPIO.setmode (GPIO.BOARD)
        GPIO.setwarnings (False)
        buzz_pin = 32
        GPIO.setup (buzz_pin,GPIO.OUT)
        Buzz = GPIO.PWM(buzz_pin,1000)
        Buzz.ChangeFrequency(25)
        Buzz.start(50)
        time.sleep(2)
        Buzz.stop( )
        GPIO.cleanup( )
    else:
        if guess > random_number:
            print 'Guess is too high'
            GPIO.setmode (GPIO.BOARD)
            GPIO.setwarnings (False)
            buzz_pin = 32
            GPIO.setup (buzz_pin,GPIO.OUT)
            Buzz = GPIO.PWM(buzz_pin,1000)
            Buzz.ChangeFrequency(1000)
            Buzz.start(50)
            time.sleep(2)
            Buzz.stop( )
            GPIO.cleanup( )
        else:
            print 'You Guessed it'
            GPIO.setmode (GPIO . BOARD)
            GPIO.setwarnings (False)
            led_pin = 11
            GPIO.setup(led_pin,GPIO.OUT)
            GPIO.output (led_pin , True)
            time.sleep(2)
            GPIO.output (led_pin , False)
            GPIO.cleanup ( )
            break
