import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def drawFunction():
     t = np.linspace(0, 5, 100)
     y_t = np.sin(t ** 2) + np.power(1 - t * np.cos(t), 1/4)
     z_t = np.log(t + 1) / np.sqrt(1 + t ** 2)
     w_t = z_t - y_t

     ax = plt.subplots()[1]
     ax.plot(t, y_t, label="sin(t^2) + (1 - t * cos(t))^1/4", linestyle=':', linewidth=4)
     ax.plot(t, z_t, label="In(t + 1)/(1 + t^2)^1/2", linestyle='--', linewidth=4)
     ax.plot(t, w_t, label="z(t) - y(t)", linestyle='-.', linewidth=4)
     ax.set_xlabel("x")
     ax.set_ylabel("y")
     ax.legend()

     plt.title("Графики функций y(t), z(t), w(t)")
     plt.grid()

def drawParametricfunction():
     t = np.linspace(0, 10, 50)
     x_t = np.sin(3 * t) * np.cos(t)
     y_t = np.sin(3 * t) * np.sin(t)

     ax = plt.subplots()[1]
     ax.plot(x_t, y_t, marker='o')
     ax.set_xlabel("x")
     ax.set_ylabel("y")
     ax.legend()

     plt.title("Трилистник")
     plt.grid()

def drawContourAndSurfaceGraph():
     x, y = np.meshgrid(np.linspace(0, np.pi, 256), np.linspace(0, np.pi, 256))
     z = (x ** 2) * np.cos(y) ** 2 - 2 * (y ** 2)

     levels = np.linspace(np.min(z), np.max(z), 50)

     ax = plt.subplots()[1]
     ax.contour(x, y, z, levels=levels)

     bx = plt.subplots(subplot_kw={"projection": "3d"})[1]
     bx.plot_surface(x, y, z, cmap=cm.Blues)
     plt.grid()

if __name__ == "__main__":
     drawFunction()
     drawParametricfunction()
     drawContourAndSurfaceGraph()
     plt.show()
