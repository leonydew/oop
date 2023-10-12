#import math libraries
from abc import ABC, abstractmethod

class NumericalIntegration(ABC):
	def __init__(self, num_points, step):
		self.num_points = num_points
		self.step = step

@abstractmethod
def calcInt(self, f, lower_limit, upper_limit):
	pass

class TrapezoidalIntegration(NumericalIntegration):
	def calcInt(self, f, lower_limit, upper_limit):
		integral_sum = f(lower_limit) + f(upper_limit)
		for i in range(1, self.num_points):
			x = lower_limit + i * self.step
			integral_sum += 2 * f(x)
		integral = (self.step / 2) * integral_sum
		return integral

class SimpsonIntegration(NumericalIntegration):
	def calcInt(self, f, lower_limit, upper_limit):
		integral_sum = f(lower_limit) + f(upper_limit)
		for i in range(1, self.num_points):
			x = lower_limit + i * self.step
			if i % 2 == 0:
				integral_sum += 2 * f(x)
			else:
				integral_sum += 4 * f(x)
			integral = (self.step / 3) * integral_sum
		return integral

# Пример подынтегральной функции
def f(x):
	return x**2

# Задаем параметры расчета
num_points = 1000
step = 0.001
lower_limit = 0
upper_limit = 1

# Создаем экземпляры классов для расчета интегралов
trapezoidal_int = TrapezoidalIntegration(num_points, step)
simpson_int = SimpsonIntegration(num_points, step)

# Сравниваем результаты численного интегрирования с аналитическим решением
analytical_solution = 1/3 # Аналитическое решение интеграла x^2 от 0 до 1 (по Ньютону-Лейбницу)
trapezoidal_result = trapezoidal_int.calcInt(f, lower_limit, upper_limit)
simpson_result = simpson_int.calcInt(f, lower_limit, upper_limit)

# Выводим результаты
print("Аналитическое решение:", analytical_solution)
print("Метод трапеций:", trapezoidal_result)
print("Метод Симпсона:", simpson_result)

