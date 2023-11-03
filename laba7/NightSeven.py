import random
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# Параметры сетки
N = 50  # Количество точек по оси z
M = 2000  # Количество точек по оси t
L = 200  # Длина области по оси z
T = 2  # Длительность наблюдения по оси t
h = L / N  # Шаг по оси z
tau = T / M  # Шаг по оси t

# Инициализация сетки
z = np.linspace(0, N+2, N+2)
t = np.linspace(0, M+2, M+2)
E = np.zeros((N+2, M+2))
H = np.zeros((N+2, M+2))

E[:, 0] = 0.1 * np.sin(np.pi * (z * h) / 50)
H[:, 0] = 0.1 * np.sin(np.pi * (z * h) / 50)

# Разностная схема
for j in range(M+1):
    # Граничные условия
    E[N+1, j] = E[1, j]
    H[N+1, j] = H[1, j]
    E[0, j] = E[N, j]
    H[0, j] = H[N, j]
    for i in range(N+1):
        E[i, j+1] = E[i, j] + (tau / h) * (H[i-1, j] - H[i, j])
        H[i, j+1] = H[i, j] + (tau / (2 * h)) * (E[i-1, j] - E[i+1, j])


# Построение графиков
plt.figure(figsize=(20, 6))

timeline = [0, M//4, M//2, 3*M//4, M]

def set_color_randomly():
    return (random.random(), random.random(), random.random())

# График E в разные моменты времени
for time in enumerate(timeline):
    plt.subplot(2, 5, time[0]+1)
    plt.grid()
    plt.plot(z, E[:, time[1]], color=set_color_randomly())
    plt.xlabel('z во время t = ' + Fraction(time[1] / M).limit_denominator().__str__())
    plt.ylabel('E')

# График H в разные моменты времени
for time in enumerate(timeline):
    plt.subplot(2, 5, time[0]+6)
    plt.grid()
    plt.plot(z, H[:, time[1]], color=set_color_randomly())
    plt.xlabel('z во время t = ' + Fraction(time[1] / M).limit_denominator().__str__())
    plt.ylabel('H')

plt.tight_layout()
plt.show()