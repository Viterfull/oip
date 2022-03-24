import RPi.GPIO as GPIO
import time
def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    while (1):
        a = input('введите число от 0 до 255\n')
        if a.isdigit() == 0:
            if a == 'q':
                break
            if a[0] == '-':
                print ('можно побольше?')
                continue
            print('можно чиселку?')
            continue

        a = float(a)
        if a % 1 != 0:
            print ('можно поцелее?')
            continue
        a = int(a)
        if a > 255:
            print ('можно поменьше?')
            continue
        
        print(f'напряжение примерно {round(a*3.3/255, 2)} вольт(не ВАТТ)')
        GPIO.output(dac, decimal2binary(a))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
