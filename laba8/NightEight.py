import random
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# Параметры сетки
N = 100  # Количество точек по оси z
M = 100  # Количество точек по оси t
L = 200  # Длина области по оси z
T = 100  # Длительность наблюдения по оси t
h = L / N  # Шаг по оси z
tau = T / M  # Шаг по оси t

# Инициализация сетки
z = np.linspace(0, N, N)
t = np.linspace(0, M, M)
E = np.zeros((N, M))
H = np.zeros((N, M))
U = np.zeros((N, M))
H_half = np.zeros(N)

E[:, 0] = 0.1 * np.sin(np.pi * (z * h) / 50) # u(z)
H[:, 0] = 0.1 * np.sin(np.pi * (z * h) / 50) # v(z)

# Разностная схема
for j in range(M - 1):
    # Граничные условия
    dE0 = -tau / h * (H[0, j] - H[-1, j])
    dH0 = -tau / h * (E[-1, j] - E[0, j])

    E[0, j+1] = E[0, j] - dE0
    H[0, j+1] = H[0, j] - dH0
    for i in range(1,N):
        E[0, j+1] = E[0, j] - dE0
        H[0, j+1] = H[0, j] - dH0

        E[i, j+1] = E[i, j] + (tau / h) * (H[i, j] - H[i, j-1])
        H[i, j+1] = H[i, j] + (tau / (2 * h)) * (E[i-1, j] - E[i, j])

for i in range(N-1):
    U[i] = (E[i+1, 0] - E[i-1, 0]) / (2 * h)
    H_half[i] = (-U[i, 0] + (tau / (4 * (h ** 2))) * (H[i + 1, 0] - 2 * H[i, 0] + H[i - 1, 0])) * (2 / tau) + H[i, 0]

# Аналитическое решение
def exact_solution(z):
    return 0.2 * np.sin(2 * np.pi * z / N) * np.cos(2 * np.pi * z / N)

exact_H = exact_solution(t)

error = np.abs(H - exact_solution(np.linspace(0, M, N)) + 1)

ax_e = plt.subplots()[1]
plt.grid()
ax_e.plot(t[:], error[:], color='green', linestyle='-')

ax = plt.subplots()[1]
plt.grid()
ax.plot(z, H_half, color='red')
ax.plot(z, H[:, 1], label='Numerical')
ax.plot(z, exact_H, label="Exact")
plt.legend()
plt.show()