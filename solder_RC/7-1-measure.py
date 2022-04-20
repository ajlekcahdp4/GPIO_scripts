import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

import dec2bin as d2b

#======================================================================
#===============================defenitions============================
#======================================================================
leds   = [21, 20, 16, 12, 7, 8, 25, 24]
dac    = [26, 19, 13, 6, 5, 11, 9, 10 ]
comp   = 4
troyka = 17

MAXVOLT = 3.3
levels  = 256
dV = MAXVOLT / levels
#======================================================================
#================================setups================================
#======================================================================
GPIO.setmode(GPIO.BCM)
GPIO.setup (leds, GPIO.OUT)
GPIO.setup (dac, GPIO.OUT)
GPIO.setup (comp, GPIO.IN)
GPIO.setup (troyka, GPIO.OUT)
#======================================================================
#===============================functions==============================
#======================================================================
def troyka_input ():
    res = GPIO.input (troyka)
    if (res == 0):
        return 0
    else:
        return 3.3

def dac_output (value):
    signal = d2b.dec2bin(value)
    GPIO.output (dac, signal)
    return signal

def adc():
    value = 0
    for i in range(7, -1, -1):
        dac_output(value + 2 ** i)
        time.sleep(0.01)
        comparatorValue = GPIO.input(comp)
        if comparatorValue == 1:
            value += 2 ** i
    return value


def leds_out (val):
    GPIO.output (leds, val)

#======================================================================
#=================================main=================================
#======================================================================

try:
    mes = []
    start_time = time.time ()
    charge = 1
    GPIO.output (troyka, 1)
    while True:
        value = adc ()
        GPIO.output (leds, d2b.dec2bin(value))
        if ((charge == 1) and (value >= 230)):
            GPIO.output (troyka, 0)
            charge = 0
        elif ((charge == 0) and (value <= 10)):
            end_time = time.time ()
            period = (end_time - start_time) / (len(mes) - 1)
            frequency = 1 / period
            mes.append (value)
            break
        mes.append (value)
        cur_volt = dV * value
        print ("mesured: digital: {:d} in volts: {:.3f}".format (value, cur_volt))
    plt.plot (mes)

    with open ("data.txt", "w") as datafile:
        for i in range (len(mes)):
            datafile.write (str(mes[i]) + '\n')
    with open ("settings.txt", "w") as settingsfile:
        settingsfile.write ("T = {:f} s\n".format (period))
        settingsfile.write ("dV = {:f} V\n".format (dV))
        settingsfile.write ("t = {:f} s\n".format (end_time - start_time))
        settingsfile.write ("frequency = {:f} Hz\n".format (frequency))
    plt.show ()
    
finally:
    GPIO.output (leds, 0)
    GPIO.output (dac, 0)
    GPIO.output (troyka, 0)
    GPIO.cleanup ()
    datafile.close()
    settingsfile.close()