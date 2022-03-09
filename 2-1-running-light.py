import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

chanels = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(chanels, GPIO.OUT)
for j in range(3):
    for i in range (0, 8):
        GPIO.output (chanels[i], 1)
        time.sleep (0.2)
        GPIO.output(chanels[i], 0)
GPIO.output(chanels, 0)
GPIO.cleanup()

