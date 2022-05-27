import math
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