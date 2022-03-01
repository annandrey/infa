import math
import cmath
from module_cos import my_cos
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg')


import matplotlib.pyplot as plt
import numpy as np


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
