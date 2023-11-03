import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import tkinter as tk
import tkinter.messagebox as mb

# Класс построения GUI
class App(tk.Tk):

     # инициализируем стартовый экран
     def __init__(self):
          super().__init__()
          buttonOne = tk.Button(self, text="Task 1", command=self.showFirstTask)
          buttonTwo = tk.Button(self, text="Task 2", command=self.showSecondTask)
          buttonThree = tk.Button(self, text="Task 3", command=self.showThirdTask)

          opts = {'padx': 40, 'pady': 5, 'expand': True, 'fill': tk.BOTH}

          buttonOne.pack(**opts)
          buttonTwo.pack(**opts)
          buttonThree.pack(**opts)

     # Проверка состояние окна
     def windowIsWorking(self, window):
           while True:
               window.update()
               if not window.winfo_exists():
                    break

     # Показ первого окна
     def showFirstTask(self):
          self.withdraw()     # Cкрытие основного окна
          root = tk.Toplevel(self)
          root.geometry("400x400")
          label_desc = tk.Label(root, text="Intersected cirles")
          label = tk.Label(root, text="1st circle")
          entry_var_list = [tk.StringVar() for _ in range(6)]
          entry_x = tk.Entry(root, textvariable=entry_var_list[0])
          entry_y = tk.Entry(root, textvariable=entry_var_list[1])
          entry_r = tk.Entry(root, textvariable=entry_var_list[2])
          label_1 = tk.Label(root, text="2nd circle")
          entry_x1 = tk.Entry(root, textvariable=entry_var_list[3])
          entry_y1 = tk.Entry(root, textvariable=entry_var_list[4])
          entry_r1 = tk.Entry(root, textvariable=entry_var_list[5])
          label_desc.pack()
          label.pack()
          entry_x.pack()
          entry_y.pack()
          entry_r.pack()
          label_1.pack()
          entry_x1.pack()
          entry_y1.pack()
          entry_r1.pack()

          # Внутренний метод для передачи в action-button
          # Метод дает возможность получать значения через entry во время выполнения
          def getAmountFromEntryes():
               x = entry_x.get()
               y = entry_y.get()
               r = entry_r.get()
               x1 = entry_x1.get()
               y1 = entry_y1.get()
               r1 = entry_r1.get()
               self.showGrapher(float(x), float(y), float(r), float(x1), float(y1), float(r1))

          enterButton = tk.Button(root, text="Calculate", command=getAmountFromEntryes)
          enterButton.pack()
          self.windowIsWorking(root)
          self.deiconify()    # Показ основного окна

     # Вызов окна с графиком внутри класса
     def showGrapher(self, shiftXOne, shiftYOne, radiusOne, shiftXTwo, shiftYTwo, radiusTwo):
          shape = Circle(shiftXOne, shiftYOne, radiusOne)        # создание кругов
          shape_1 = Circle(shiftXTwo, shiftYTwo, radiusTwo)

          graph = Graph(-np.abs(shiftXOne - shiftXTwo) - (radiusOne + radiusTwo),\
                        np.abs(shiftXOne - shiftXTwo) + (radiusOne + radiusTwo),\
                        -np.abs(shiftYOne - shiftYTwo) - (radiusOne + radiusTwo),\
                        np.abs(shiftYOne - shiftYTwo) + (radiusOne + radiusTwo),\
                        1000)

          graph.drawCircle(shape)
          graph.drawCircle(shape_1)
          self.show_info(shape.intersection(shape_1))
          graph.show()

     # Вызов второго окна
     def showSecondTask(self):
          self.withdraw()
          root = tk.Toplevel(self)
          root.geometry("400x400")
          entry_var_list = tk.StringVar()
          entry = tk.Entry(root, textvariable=entry_var_list)

          # Внутренний метод для передачи в action-button
          # Метод дает возможность получать значения через entry во время выполнения
          def getAmountFromEntryes():
               x = entry.get()
               self.show_info(checkIsEvenOrNotInSumOfNumbers(int(x)))

          entryButton = tk.Button(root, text="Calculate", command=getAmountFromEntryes)
          entry.pack()
          entryButton.pack()
          self.windowIsWorking(root)
          self.deiconify()

     # Вызов третьего окна
     def showThirdTask(self):
          self.withdraw()
          root = tk.Toplevel(self)
          root.geometry("400x400")
          entry_var_list = tk.StringVar()
          entry = tk.Entry(root, textvariable=entry_var_list)

          # Внутренний метод для передачи в action-button
          # Метод дает возможность получать значения через entry во время выполнения
          def getAmountFromEntryes():
               x = entry.get()
               self.show_info(checkIsAmountOfDividersAreEvenOrNot(int(x)))

          entryButton = tk.Button(root, text="Calculate", command=getAmountFromEntryes)
          entry.pack()
          entryButton.pack()
          self.windowIsWorking(root)
          self.deiconify()

     # Вызов всплывающего окна
     def show_info(self, text):
          self.withdraw()
          mb.showinfo("Is...", text)

# Базовый класс для фигур

class Shape:
     def __init__(self, shift_x=0, shift_y=0):
          self.__shift_x = shift_x
          self.__shift_y = shift_y

     # геттеры-сеттеры для базового класса
     def setShiftByAxisX(self, shift_x):
          self.__shift_x = shift_x

     def setShiftByAxisY(self, shift_y):
          self.__shift_y = shift_y

     def getShiftByAxisX(self):
          return self.__shift_x

     def getShiftByAxisY(self):
          return self.__shift_y

     # перегружаемый метод для наследуемых классов(не знаю зачем)
     def intersection(self):
          pass

# Наследуемый класс
class Circle(Shape):

     def __init__(self, shift_x=0, shift_y=0, radius=1):
          Shape.__init__(self, shift_x, shift_y)
          self.__radius = radius

     # вспомогательные геттеры-сеттеры для наследуемого класса
     def setRadius(self, radius):
          self.__radius = radius

     def getRadius(self):
          return self.__radius

     def distance(self, shape):
          return np.sqrt((self.getShiftByAxisX() - shape.getShiftByAxisX()) ** 2 + (self.getShiftByAxisY() - shape.getShiftByAxisY()) ** 2)

     # Определить, пересекаются ли две окружности. Вводятся 6 чисел: две тройки чисел(x, y, R) - координаты центра и радиус окружности
     # Если мин окружность меньше расстояния центров, проверим суммой длины мин рад и расстояния точек
     # if min_rad + dist < max_rad (внутри окружности) False
     def intersection(self, shape):
          if self.distance(shape) <= (self.getRadius() + shape.getRadius()):
               if min(self.getRadius(), shape.getRadius()) + self.distance(shape) \
                    >= max(self.getRadius(), shape.getRadius()):
                    return "Yes"
          return "No"

# Класс для вызова окна с графиком
class Graph:

     # настраиваем окно для отрисовки графики
     def __init__(self, leftX=-10, rightX=10, leftY=-10, rightY=10, accurate=100):
          self.x = np.linspace(leftX, rightX, accurate)
          self.y = np.linspace(leftY, rightY, accurate)
          self.a, self.b = np.meshgrid(self.x, self.y) # Вызываем этот метод, т.к. в нашем графике есть две точки с одинаковыми аргументами
          self.axes = plt.subplots()[1]

     # Отрисовка круга
     def drawCircle(self, shape):
          C = (self.a - shape.getShiftByAxisX()) ** 2 + (self.b - shape.getShiftByAxisY()) ** 2 - shape.getRadius() ** 2
          self.axes.contour(self.a, self.b , C, [0])
          self.axes.set_aspect(1)

     # Показ окна графика
     def show(self):
          plt.show()

# Дано натуральное число. Проверьте, является ли сумма его цифр четной или нечетной. Выведите odd или even.
def checkIsEvenOrNotInSumOfNumbers(number):
     temp = 1
     sum = 0
     while number >= temp:
          temp_num = number
          sum += int(temp_num / temp) % 10
          temp *= 10

     print("Sum: %d" %sum)

     if sum % 2 == 0 and sum != 0:
          return "even"

     return "odd"

# Дано натуральное число. Выяснить, является ли количество его делителей четным или нечетным. Вывести even или odd.
def checkIsAmountOfDividersAreEvenOrNot(number):
     temp = number
     sum = 0
     counter = 1
     while counter <= int(number):
          if(number % counter == 0):
               sum += 1
               print(counter)
          counter += 1

     print("Sum: %d" %sum)

     if sum % 2 == 0:
          return "even"

     return "odd"

if __name__ == "__main__":
     app = App()
     app.mainloop()