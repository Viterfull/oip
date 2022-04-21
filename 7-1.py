import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt


GPIO.setmode(GPIO.BCM)   
# массивы с  пинами и нужными для работы данными
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
comp = 4
arr = [0]*8
troyka = 17
datad = [] #сюда сохраняются данные

#настройка пинов
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    '''
        перевод числа в двоичный код в формате массива
    '''
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def abc():
    '''
        взятие значения на тройке
    '''
    GPIO.output(dac, 0)
    for i in range(8):
        GPIO.output(dac[i], 1)
        arr[i] = 1
        time.sleep(0.005)
        if GPIO.input(comp) == 0:
            GPIO.output(dac[i], 0)
            arr[i] = 0
    arr.reverse()
    g = 0
    for i in range(8):
        g += 2**i*arr[i]
    return g
try:
    GPIO.output(troyka, 1)
    v = 0
    volt = 0
    kolvo = 0
    start_time = time.time()#запись времени
    #расчеты при зарядке
    while(volt < 3.15):
        kolvo += 1
        v = 0
        GPIO.output(dac, decimal2binary(abc()))
        v = abc()
        volt = v*3.3/256
        print('отсчет' ,v, 'вольты', volt)
        datad.append(v) #запись данных
        #зелененькая подсветка 
        GPIO.output(leds, 0)
        for k in range(9):
            if(v < k * 32 + 5):
                j = 0
                for j in range(k):
                    GPIO.output(leds[j], 1)
                break
    GPIO.output(troyka, 0)
    while(volt > 0.1):
        v = 0
        kolvo = kolvo + 1
        GPIO.output(dac, decimal2binary(abc()))
        v = abc()
        volt = v*3.3/256
        print('отсчет' ,v, 'вольты', volt)
        datad.append(v) #запись данных
        #зелененькая подсветка 
        GPIO.output(leds, 0)
        for k in range(9):
            if(v < k * 32 + 5):
                j = 0
                for j in range(k):
                    GPIO.output(leds[j], 1)
                break 
    #расчеты времяни и печать данных
    sec = time.time() - start_time
    T = sec / kolvo
    print("--- t = %s seconds ---" % sec)
    print("--- T = %.3f seconds ---" % T)
    print("--- v = %.3f Hz ---" %  (1/T))
    print("--- dV = %.3f volts ---" % float(3.3/256))
    sets = []
    sets.append((1/T))
    sets.append(3.3/256)
    set_str = [str(i) for i in sets]  
    data_str = [str(item) for item in datad]  
    #вывод графика
    plt.plot(datad)
    plt.show()
    #сохранение в файл
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(data_str)) 
    with open("settings.txt", "w") as set:
        set.write("\n".join(set_str))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
