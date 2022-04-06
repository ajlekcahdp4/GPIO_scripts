import RPi.GPIO as GPIO
import dec2bin as d2b
import time


dac    = [26, 19, 13, 6, 5, 11, 9, 10]
comp   = 4
troyka = 17
levels = 256
MAXVOLT = 3.3
digits = 8
output = [0] * digits


def adc ():
    value = 0
    for i in reversed(range(digits)):
        b_value = d2b.dec2bin (value + 2**i)
        GPIO.output(dac, b_value)
        time.sleep(0.01)
        comp_value = GPIO.input(comp)
        if (comp_value == 1):
            value += 2**i
    return value

            

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
