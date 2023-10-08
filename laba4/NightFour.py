import time
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

def create_matrix():
     np.set_printoptions(suppress=True, precision=3)
     index = 2
     matrix_a = np.pad(np.diag(np.linspace(6, 1, num=6)), ((1, 0), (0, 1)), mode='constant')
     diag_matrix_of_eight = np.diag(np.full(7, 8))
     matrix_a = matrix_a + diag_matrix_of_eight
     matrix_a[index] = np.full(7, 5)
     exp_matrix_a = np.pad(np.exp(matrix_a), ((7, 0), (7, 0)), mode="constant")
     matrix_a = np.pad(matrix_a, ((0, 7), (0, 7)), mode="constant")
     zero_matrix = np.zeros((14, 14))
     ones_matrix = np.pad(np.diag(np.ones(7)), ((0, 7), (7, 0)), mode="constant")
     np.savetxt('savetxt.txt', exp_matrix_a \
                             + zero_matrix \
                             + matrix_a \
                             + ones_matrix, fmt='%d')

def vectorized_sum(N, x):
     if x==0:
         raise ZeroDivisionError("Divition by zero")

     i = np.arange(0, N)

     start_time = time.time()

     try:
          sqrt_ix = np.sqrt(i + x**2)
     except ZeroDivisionError as e:
          print(str(e))

     sin_x = np.sin(x)
     sin_ix = np.sin(i * x)
     sqrt_ix = np.sqrt(i + x**2)

     end_time = time.time()

     sum = np.sum((sin_x * sin_ix) / sqrt_ix)
     return (sum, end_time - start_time)

def cyclic_sum(N, x):

    if x==0:
         raise ZeroDivisionError("Divition by zero")

    total_sum = 0.0
    start_time = time.time()

    try:
          for i in range(0, int(N)):
                    total_sum += np.sin(x) * np.sin(i * x) / np.sqrt(i + x**2)
    except ZeroDivisionError as e:
          print(str(e))

    end_time = time.time()
    return (total_sum, end_time-start_time)


def task_three():
     matrix = np.loadtxt("savetxt.txt")

     def diff(amount):
          return (amount > -3) & (amount < 4)

     temp = filter(diff, matrix[:, 0])
     sum = reduce(lambda x, y : np.abs(x) + np.abs(y), temp, 0)
     return sum

def show_difference_on_display():
     x = np.linspace(0, 1000, num=1001)
     y1 = [cyclic_sum(i, 2)[1] for i in x]
     y2 = [vectorized_sum(i, 2)[1] for i in x]
     z1 = [cyclic_sum(i, 2)[0] for i in x]
     z2 = [vectorized_sum(i, 2)[0] for i in x]
     fig, ax = plt.subplots()
     fig, ax1 = plt.subplots()
     fig, ax2 = plt.subplots()
     ax.plot(x, y1, label='cyclic_sum')
     ax.plot(x, y2, label='vectorized_sum')
     ax1.plot(x, z1, label="sum_1")
     ax2.plot(x, z2, label="sum_2", color='orange')
     ax.legend()
     ax1.legend()
     plt.show()

if __name__ == "__main__":
     # create_matrix()
     # N, x = [int(input()) for _ in range(2)]
     # print(vectorized_sum(N, x))
     # print(cyclic_sum(N, x))
     # show_difference_on_display()
     # print("sum of collum:", task_three())
     print(task_three())