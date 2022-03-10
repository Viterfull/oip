import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

lebs = [21, 20, 16, 12, 7, 8, 25, 24]

def test():
    for i in lebs:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)

GPIO.setup(lebs, GPIO.OUT)

for i in range(3):
    test()

GPIO.output(lebs, 0)
GPIO.cleanup()