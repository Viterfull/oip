import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

lebs = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

GPIO.setup(lebs, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

GPIO.output(lebs, 0)
GPIO.cleanup()