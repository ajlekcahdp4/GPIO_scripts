import RPi.GPIO as GPIO
import dec2bin as d2b
import time
import input_check as IC

#========================================================================
#=================================main()=================================
#========================================================================
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    period_str = input ("Please, enter the period\n")
    res = IC.InputCheck(period_str)
    if res:
        period = int (period_str)
        val = 0
        while True:
            while val < 255:
                val += 1
                GPIO.output(dac, d2b.dec2bin(val))
                time.sleep (period/512)
            while val > 0:
                val -= 1
                GPIO.output(dac, d2b.dec2bin(val))
                time.sleep (period/512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()