import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]

prow = [255, 127, 64, 32, 5, 0]

def give_binary(a):
    a = str(format(int(a), "08b"))
    b = []
    for i in a:
        b.append(int(i))
    return b



GPIO.setup(dac, GPIO.OUT)

for i in prow:
    GPIO.output(dac, give_binary(i))
    time.sleep(10)



GPIO.output(dac, 0)
GPIO.cleanup()