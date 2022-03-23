import RPi.GPIO as GPIO
import input_check as IC

#========================================================================
#=================================main()=================================
#========================================================================
GPIO.setmode(GPIO.BCM)


out = 22

GPIO.setup (out, GPIO.OUT)
p = GPIO.PWM(out, 50)
p.start (0)
try:
    while True:
        coef_str = input ("Please, enter the coefficiant of duty cycle\n")
        res = IC.InputCheck(coef_str)
        if res:
            coef = int (coef_str)
            p.ChangeDutyCycle(coef)
except KeyboardInterrupt:
    print ("KeyboardInterrupt\n")
finally:
    p.stop()
    GPIO.cleanup()