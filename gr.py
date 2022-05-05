import matplotlib.pyplot as plt
import numpy as np
import math


# data = np.array([1, 1, 6, 1, 1])
# N = 10
# dt = 0.5
# print(np.linspace(0 ,  dt*N,  N))
# print(np.arange( 0 ,  N,  dt))


with open('settings.txt') as f:
    step = float(f.readline())
    T = float(f.readline())

data = np.loadtxt('data.txt')
data = data * step
n = len(data)
t = np.linspace(0, n*T, n)

plt.plot(t, data, label = 'V(t)', c = 'g')
plt.scatter(t[::30],data[::30], c = 'g')
plt.xlabel('Время, c')
plt.ylabel('напряжение, В')
plt.title('Процесс заряда и разряда конденсатора в RC цепи')
plt.grid(which='major')
plt.grid(which='minor', linestyle=':')
plt.text(6, 2.5, f'Время заряда = {t[data.argmax()]:.2}')
plt.text(6, 2, f'Время разряда = {t[-1]-t[data.argmax()]:.2}')
plt.savefig('gr.svg')
plt.show()





# x = [1/(x + 273) for x in t]
# _, fig = plt.subplots()
# k1 = []
# fig.set_title("зависимость $ln(P)$ от $\\frac{1}{T}$")
# fig.set_ylabel("$ln(P)$")
# fig.set_xlabel("$\\frac{1}{T}$")
# fig.minorticks_on()
# fig.grid(which='major')
# fig.grid(which='minor', linestyle=':')
# fig.legend(fontsize = 10)
# plt.show()
