#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat( )
import time
import random

x = random.randint(0,7)
y = random.randint(0,7)
r = random.randint(1,255)
g = random.randint(1,255)
b = random.randint(1,255)

sense.set_pixel(x, y, (r, g, b))

time.sleep(1)
sense.clear ( )
