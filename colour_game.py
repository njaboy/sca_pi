#!/usr/bin/env python
import RPi.GPIO as GPIO
from sense_hat import SenseHat
sense = SenseHat ( )
L = 1
saying = 'just do it'
text = (0, 0, 0)
back = (50, 50, 50)
speed = 0.01
while L < 10:
    message = saying
    sense.show_message(message, speed, text_colour=text, back_colour=back)
    guess = (raw_input("Guess The saying: "))
    if guess != saying:
        print 'Wrong Please Try Agian'
        L = L + 1
        speed = speed + .01
    else:
        print 'You Guessed it'
        print speed
        break
sense.clear ( )
