from numpy import array
from numpy.linalg import norm, det
from numpy.linalg import solve as solve_out_of_the_box
from numpy.random import uniform
N=100
SMALL = 1e-5
def test_error(solver_function):
    # Сгенерируем хорошо обусловленную систему
    while True:
        a = uniform(0.0, 1.0, (N, N))
        b = uniform(0.0, 1.0, (N,  ))

        d = det(a)
        if abs(d) <= SMALL:  # Определитель маленький — плохо
            # print(f"det: {d}")
            continue  # Попробуем ещё
        if d < 0.0:  # Отрицательный — поменяем знак
            # print(f"det: {d}")
            a = -a

        try:
            oob_solution = solve_out_of_the_box(a, b)
        except Exception as e:  # Всё-таки система плохая
            # print(f"exc: {e}")
            continue  # Попробуем ещё

        sb = a @ oob_solution
        if norm(sb - b, ord=1) > SMALL:
            # print("Bad solution...")
            continue  # Всё же не очень система получилась =)
        
        break # Всё, считаем, что мы случайно сгенерировали хорошую систему

    tested_solution = solver_function(a, b)
    return norm(tested_solution - oob_solution, ord=1)
def gauss(a, b):
    a = a.copy()
    b = b.copy()
    def forward():
        """
        Функция, которая приводит матрицу к виду верхней треугольной
        Параметры:
        ----------
        i: int
            номер строки
        j: int
            номер столбца
        """   
        for i in range(len(a)):
            b[i] /= a[i][i]
            a[i] /= a[i][i]
            for j in range(i+1, len(a)):
                b[j] -= b[i]*a[j][i]
                a[j] -= a[i]*a[j][i]
    def backward():
        """
        Функция, которая ищет решения СЛАУ
        Параметры:
        ----------
        i: int
            номер строки
        j: int
            номер столбца
        """   
        for i in range (-1, -len(a) - 1, -1):
            for j in range (-1, i, -1):
                b[i] -= a[i][j]*b[j]
    forward()
    backward()
    return b
    
a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)
b = array([
    [5],
    [6],
    [7],
    [8]
    ], dtype=float)
ab = array([
    [1.5, 2.0, 1.5, 2.0, 5.0],
    [3.0, 2.0, 4.0, 1.0, 6.0],
    [1.0, 6.0, 0.0, 4, 7.0],
    [2.0, 1.0, 4.0, 3, 8.0]
    ],dtype=float)
print(test_error(gauss))
