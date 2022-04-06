import RPi.GPIO as GPIO
import dec2bin as d2b
import time


dac    = [26, 19, 13, 6, 5, 11, 9, 10]
comp   = 4
troyka = 17
levels = 256
MAXVOLT = 3.3

def adc ():
    for value in range (256):
        signal = d2b.dec2bin(value)
        GPIO.output(dac, signal)
        time.sleep(0.01)
        comp_val = GPIO.input(comp)
        if comp_val == 0:
            return int(value)

#========================================================================
#==================================main==================================
#========================================================================


GPIO.setmode(GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)




try:
    while True:
        value = adc ()
        V_val = value / levels * MAXVOLT
        print ("{:3d} -> {:.3f} V".format (value, V_val))
finally:
    GPIO.output (dac, 0)
    GPIO.output (troyka, 0)
    GPIO.cleanup()
