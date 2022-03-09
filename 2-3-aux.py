import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [2, 3, 14, 15, 18, 27,23, 22]
GPIO.setup (leds, GPIO.OUT)
GPIO.setup (aux, GPIO.IN)

while True:
    for i in range (0, 8):
        GPIO.output (leds[i], GPIO.input(aux[i]))
        time.sleep (0.2)                                                                                                                                                                                                                                                                           