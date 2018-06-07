#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat ( )

text = (0, 0, 0)
back = (0, 0, 255)

speed = 0.1

message = "Have a Nice Day"

sense.show_message(message, speed, text_colour=text, back_colour=back)

sense.clear ( )
