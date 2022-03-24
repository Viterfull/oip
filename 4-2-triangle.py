import RPi.GPIO as GPIO
import time
def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
5
try:
    T = float(input())/510
    while (1):
        for i in range(256):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(T)
        for i in range(254, 0, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(T)
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
