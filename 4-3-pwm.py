import RPi.GPIO as GPIO
import time
def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
lebs = [21, 20, 16, 12, 7, 8, 25, 24]
pin = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
sh = GPIO.PWM(pin, 1000)
sh.start(0)
try:
    while (1):
        a = float(input(('введите % мощьности\n')))
        sh.ChangeDutyCycle(a)
        print (f'вольтов всего {3.3*a/100}')
        
finally:
    GPIO.output(pin, 0)
    GPIO.cleanup()
