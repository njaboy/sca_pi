import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)

buzz_pin = 32

GPIO.setup (buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

def buzz (freq) :
        Buzz.ChangeFrequency(freq)
        Buzz.start(50)
        time.sleep(.1)
        Buzz.stop( )

buzz (660)
buzz (510)
buzz (660)
buzz (770)
buzz (380)
buzz (510)
buzz (380)
buzz (320)
buzz (440)
buzz (480)
buzz (450)
buzz (430)
buzz (380)
buzz (660)
buzz (760)
buzz (860)
buzz (700)
buzz (760)
buzz (660)
buzz (520)
buzz (580)
buzz (480)
buzz (510)
buzz (380)

GPIO.cleanup( )
