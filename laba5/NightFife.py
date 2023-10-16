import numpy as np
import numpy.polynomial as polynomial
import matplotlib.pyplot as plt

# Задание 1. Для матрицы А из задания 1 лабораторной №4 найти собственные
# значения и собственные векторы. Для наименьшего по модулю собственного значения
# проверить равенство Аx = lambda*x.
def findOwnAmountsAndVectorsForMatrix(matrix):
    eigen_values, eigen_vectors = np.linalg.eig(matrix)

    min_value = min(eigen_values, key=abs)
    index = np.where(np.isclose(eigen_values, min_value))[0][0]
    eigen_vector = eigen_vectors[:, index]

    def check_equation():
       rhs = matrix @ eigen_vector
       lhs = min_value * eigen_vector
       return np.allclose(rhs, lhs)

    if check_equation():
        print(f"Собственное значение {min_value} удовлетворяет условию Ax = λx для собственного вектора {eigen_vector}.")
    else:
        print(f"Собственное значение {min_value} НЕ удовлетворяет условию Ax = λx для собственного вектора {eigen_vector}.")

# Задание 2. Для интегрирования использовать библиотеку numpy.polynomial.

def onePoly(index=0):
    return polynomial.Polynomial([0] * (index) + [1])

def scalarMulty(func):
    res = func.integ()
    return res(1) - res(0)

def approximateFunction():
    a = np.array([[scalarMulty(*polynomial.polynomial.polymul(onePoly(i), onePoly(k))) for i in range(1, 7)] for k in range(1, 7)])
    b = np.array([scalarMulty(*polynomial.polynomial.polymul(onePoly(7), onePoly(k))) for k in range(1, 7)])

    result = np.linalg.solve(a, b)

    app_func = polynomial.Polynomial(result)
    x = np.linspace(-1, 2, 1000)
    y = app_func(x)
    y1 = onePoly(7)(x)

    ax = plt.subplots()[1]
    ax.plot(x, y, label="approximate")
    ax.plot(x, y1, label="X^7")
    ax.legend()
    plt.show()

#  Создать функцию с переменным количеством аргументов, которая:
# 1) либо в качестве аргументов принимает матрицу С и вектор b и решает систему
# Cx = b,
# 2) либо принимает только матрицу С, а вектор b формирует случайным образом
# (используя указанное в варианте распределение) и решает ту же систему.
# Функция возвращает два аргумента: решение и указанную в варианте норму.
# Предварительно проверить, является ли матрица C невырожденной.
# Вариант 6. Нормальное распределение с математическим ожиданием –1 и
# среднеквадратическим отклонение 2; октаэдрическая норма.

def solve_linear_system(matrix, *args):
    mu = -1
    sigma = 2
    n = matrix.shape[1]

    if len(args) == 0:
        b = np.random.normal(mu, sigma, n)
    elif len(args) == matrix.shape[1]:
        b = np.array(args)
    elif len(args < matrix.shape[1]):
        print("Добавлены элементы в количестве: {n - len(args)} штук")
        b = np.concatenate((tuple(args), (np.random.normal(mu, sigma, n - len(args)))))
    else:
        print("Неверное количество аргументов.")
        return None

    if np.linalg.det(matrix) == 0:
        print("Матрица C является вырожденной. Система не имеет единственного решения.")
        return None

    res = np.linalg.solve(matrix, b)

    octa_norm = sum([abs(val) for val in res])

    return res, octa_norm

if __name__ == "__main__":
    matrix = np.loadtxt("laba5/savetxt.txt")
    # matrix = np.array([[1, 2, 3],
    #                [4, 5, 6],
    #                [7, 8, 9]])
    approximateFunction()
    findOwnAmountsAndVectorsForMatrix(matrix)
    print(solve_linear_system(matrix))