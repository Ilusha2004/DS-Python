import numpy as np
import numpy.polynomial as polynomial
import matplotlib.pyplot as plt
from scipy import integrate

# Задание 1. Для матрицы А из задания 1 лабораторной №4 найти собственные
# значения и собственные векторы. Для наименьшего по модулю собственного значения
# проверить равенство Аx = lambda*x.
def findOwnAmountsAndVectorsForMatrix():
    # matrix = np.loadtxt("laba4/savetxt.txt")
    matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
    eigen_amount, eigen_vectors = np.linalg.eig(matrix)
    
    print(list(eigen_vectors))
    
    min_eigen = min(abs(eigen_amount))
    print(min_eigen)
    
    def check_equation(eigen_vector):
        print(np.round(np.multiply(matrix, eigen_vector), decimals=3), np.round(eigen_amount * eigen_vector, decimals=3))
        return np.round(np.multiply(matrix, eigen_vector), decimals=3) == np.round(eigen_amount * eigen_vector, decimals=3)
        
    temp = map(check_equation, list(eigen_vectors))
    print(list(temp))
   

# Задание 2. Для интегрирования использовать библиотеку numpy.polynomial.

def onePoly(index=0):
    return polynomial.Polynomial([0] * (index) + [1]) 

def scalarMulty(func):
    res, err = integrate.quad(func, 0, 1)
    return res, err

def aproximateFunction():
    a = np.array([[scalarMulty(*polynomial.polynomial.polymul(onePoly(i), onePoly(k)))[0] for i in range(0, 7)] for k in range(0, 7)])
    
    b = np.array([scalarMulty(*polynomial.polynomial.polymul(onePoly(7), onePoly(k)))[0] for k in range(0, 7)])
    result = np.linalg.solve(a, b)
    
    app_func = polynomial.Polynomial(result)
    x = np.linspace(-1, 1, 1000)
    y = app_func(x)
    y1 = onePoly(7)(x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(x, y1)
    ax.legend()
    plt.show()
    
    
# Задание 3. Создать функцию с переменным количеством аргументов, которая:
# Вариант 6. Нормальное распределение с математическим ожиданием –1 и
# среднеквадратическим отклонение 2; октаэдрическая норма.


if __name__ == "__main__":  
    aproximateFunction()