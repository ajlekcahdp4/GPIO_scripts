import RPi.GPIO as GPIO
import dec2bin as d2b
import time

def PrintVolt (val):
    volt = 3.3 * (val / 255)
    print ("{:.3f} V".format(volt))
#========================================================================
def isfloat (val_str):
    try:
        float (val_str)
        return True
    except ValueError:
        return False

#========================================================================
def InputCheck (val_str):
    if val_str.isdigit():
        return 1
    elif isfloat(val_str):
        val_float = float (val_str)
        if val_float < 0:
            print ("ERROR: anegative number was entered\n")
        else:
            print ("ERROR: float number was entered\n")
        return 0
    elif val_str != "q":
        print ("ERROR: Not a number was entered\n")
        return 0
#========================================================================
#=================================main()=================================
#========================================================================
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    val_str = input ("Please, enter the number in range (0, 255)\n")
    res = InputCheck(val_str)
    if res == 1:
        val = int(val_str)
        bin_val = d2b.dec2bin(val)
        GPIO.output(dac, bin_val)
        time.sleep(2)
        PrintVolt (val)
except ValueError:
    print ("ERROR\n")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()