#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat( )

r = (255, 0, 0)
b = ( 0, 0, 255)
w = (255, 255, 255)

pixels = [
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
]

sense.set_pixels(pixels)
