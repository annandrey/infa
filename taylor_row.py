import math
import cmath
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg')


import matplotlib.pyplot as plt
import numpy as np

ITERATIONS = 20
def my_cos(x):
    """
    Вычисление синуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    x_pow = 1
    partial_sum = 0
    for n in range(0, ITERATIONS):
        partial_sum+= ((-1)**n)*(x_pow/math.factorial(2*n)) 
        x_pow *= x**2
    return partial_sum
print(math.cos(0.8))
print(my_cos(0.8))
complex_angle = cmath.acos(5)
print('"Угол", на котором косинус достигает пяти:', complex_angle)

print("Достигает ли пяти наш косинус?", my_cos(complex_angle))
print("А библиотечный?", cmath.cos(complex_angle))

angles = np.arange(-8.25, 8.25, 0.01)
plt.plot(angles, [math.cos(x) for x in angles])
plt.plot(angles, [my_cos(x) for x in angles])
plt.show()
