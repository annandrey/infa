import cmath
import math

import matplotlib.pyplot as plt
import numpy as np
import My_cos

print(math.cos(0.8))
print(My_cos.my_cos(0.8))
complex_angle = cmath.acos(5)
print('"Угол", на котором косинус достигает пяти:', complex_angle)

print("Достигает ли пяти наш косинус?", My_cos.my_cos(complex_angle))
print("А библиотечный?", cmath.cos(complex_angle))

angles = np.arange(-8.25, 8.25, 0.01)
plt.plot(angles, [math.cos(x) for x in angles])
plt.plot(angles, [My_cos.my_cos(x) for x in angles])
plt.show()
