import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def abc():
    for i in range (256):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            return i
    return 0

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

try:
    while 1:
        v = abc()
        print(f'{v} => {v*3.3/256}')
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()