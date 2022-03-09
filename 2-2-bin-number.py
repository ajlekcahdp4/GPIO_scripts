import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

DAC = [26, 19, 13, 6, 5, 11, 9, 10]

numb = [0, 0, 0, 0, 0, 1, 0, 1]

GPIO.setup(DAC, GPIO.OUT)

GPIO.output (DAC, numb)
time.sleep (15)
GPIO.output (DAC, 0)
GPIO.cleanup()
