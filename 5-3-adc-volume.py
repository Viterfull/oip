import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
lebs = [21, 20, 16, 12, 7, 8, 25, 24]
arr = [0]*8
comp = 4
troyka = 17

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def abc():
    GPIO.output(dac, 0)
    for i in range(8):
        GPIO.output(dac[i], 1)
        arr[i] = 1
        time.sleep(0.01)
        if GPIO.input(comp) == 0:
            GPIO.output(dac[i], 0)
            arr[i] = 0
    arr.reverse()
    g = 0
    for i in range(8):
        g += 2**i*arr[i]
    return g


GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(lebs, GPIO.OUT)

try:
    while 1:
        v = abc()
        print(f'{v} => {v*3.3/256}')
        col = round(v/256*8, 0)
        if col != 0:
            j = 0
            for i in range(int(col)):
                GPIO.output(lebs[i], 1)
                j = i+1
            for i in range(j, 8):
                GPIO.output(lebs[i], 0)
        else:
            GPIO.output(lebs, 0)
            


        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()