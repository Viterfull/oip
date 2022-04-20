import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt


GPIO.setmode(GPIO.BCM)   

dac = [26, 19, 13, 6, 5, 11, 9, 10]
cad = [10, 9, 11, 5, 6, 13, 19, 26]
mas = [0, 0, 0, 0, 0, 0, 0, 0]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
led = []
comp = 4
troyka = 17
datad = []

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

i = 0
def adc():
    
    for i in 7, 6, 5, 4, 3, 2, 1, 0:
        #print(i)
        GPIO.output(cad[i], 1)
        mas[7 - i] = 1
        time.sleep(0.007)
        if(GPIO.input(comp) == 0):
            GPIO.output(cad[i], 0)
            mas[7-i] = 0
try:
    GPIO.output(troyka, 1)
    v = 0
    volt = 0
    p = 0
    kolvo = 0
    start_time = time.time()
    while(volt < 3.15):
        #v = adc()
        #if(p == 0):     
            #onesec = time.time()
        #onesec = time.time()
        kolvo = kolvo + 1
        v = 0
        mas = [0, 0, 0, 0, 0, 0, 0, 0]
        GPIO.output(dac, mas)
        adc()
        for j in range(8):
            v += mas[j]*(2**(7-j))
        volt = v*3.3/256
        print(v, "  ", volt)
        datad.append(volt) 
        GPIO.output(leds, 0)
        k = 0
        for k in range(9):
            if(v < k * 32 + 5):
                j = 0
                for j in range(k):
                    GPIO.output(leds[j], 1)
                    #print(j)
                break
        #if(p == 0):     
            #twosec = time.time()
            #p = 1
    GPIO.output(troyka, 0)
    while(volt > 0.1):
        #v = adc()
        v = 0
        mas = [0, 0, 0, 0, 0, 0, 0, 0]
        kolvo = kolvo + 1
        GPIO.output(dac, mas)
        adc()
        for j in range(8):
            v += mas[j]*(2**(7-j))
        volt = v*3.3/256
        print(v, "  ", volt)
        datad.append(volt) 
        GPIO.output(leds, 0)
        k = 0
        for k in range(9):
            if(v < k * 32 + 5):
                j = 0
                for j in range(k):
                    GPIO.output(leds[j], 1)
                    #print(j)
                break 
    sec = time.time() - start_time
    T = float(sec) / kolvo
    print(kolvo)
    print("--- t = %s seconds ---" % sec)
    print("--- T = %f seconds ---" % T)
    print("--- v = %f Hz ---" %  (float(1)/T))
    print("--- dV = %f volts ---" % float(3.3/256))
    sets = []
    sets.append((float(1)/T))
    sets.append(float(3.3/256))
    set_str = [str(i) for i in sets]  
    data_str = [str(item) for item in datad]  
    plt.plot(datad)
    plt.show()
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(data_str))  
        #outfile.write("\n".join(sec))
    with open("settings.txt", "w") as set:
        set.write("\n".join(set_str))  
        #outfile.write("\n".join(sec))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
