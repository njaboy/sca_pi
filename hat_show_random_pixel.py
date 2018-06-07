#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat( )
import time
import random
T = 1
while T < 300:
    T = T + 1
    x = random.randint(0,7)
    y = random.randint(0,7)
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    sense.set_pixel(x, y, (r, g, b))

    time.sleep(.1)
sense.clear ( )
