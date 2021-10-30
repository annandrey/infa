from matplotlib import pyplot as pp

MODEL_G = 9.81
MODEL_DT = 0.01
VELOCITY_OF_EXHAUST = 3660
class Body:
    def __init__(self, x, y, v_x, v_y, m):
        """
        Создать тело.
        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        v_x: float
            горизонтальная скорость
        v_y: float
            вертикальная скорость
        """
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.m = m
        self.trajectory_x = []
        self.trajectory_y = []
    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        self.x += self.v_x * MODEL_DT
        self.y += self.v_y * MODEL_DT
        self.v_y -= MODEL_G * MODEL_DT
class Rocket(Body):
    def __init__(self, x, y, m_body, m_fuel, m_dt):
        """
        Создать ракету.
        Параметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        m_body: float
           масса корпуса ракеты
        m_fuel: float
           масса топлива
        m_dt: float
           изменение массы( выброс топлива )
        """
        super().__init__(x, y, 10, 10, m_fuel + m_body) # Вызовем конструктор предка — тела
        self.m_fuel = m_fuel
        self.m_dt = m_dt
    def advance(self):
        """
        Выполним шаг математической модели ракеты
        """
        super().advance() # вызовем метод предка — тела, т.к. и он для ракеты актуален.

        if(self.m_fuel >= self.m_dt * MODEL_DT):
            self.m_fuel -= self.m_dt * MODEL_DT # вычтем массу сгоревшего топлива
            accel = (self.m_dt * VELOCITY_OF_EXHAUST)/self.m# найдем ускорение ракеты
            accel_x = accel * (self.x/(self.x**2 + self.y**2)) # найдем проекцию ускорения на ось х
            accel_y = accel * (self.y/(self.x**2 + self.y**2)) # найдем проекцию ускорения на ось у
            self.v_x += accel_x # запишем приращение скорости для оси х и у
            self.v_y += accel_y
        elif(self.m_fuel > 0 and self.m_fuel < self.m_dt * MODEL_DT):
            self.m_fuel = 0
            accel = (self.m_dt * VELOCITY_OF_EXHAUST)/self.m
            accel_x = accel * (self.x/(self.x**2 + self.y**2))
            accel_y = accel * (self.y/(self.x**2 + self.y**2))
            self.v_x += accel_x
            self.v_y += accel_y
rocket1 = Rocket(0, 0, int(input("Body mass")), int(input("Fuel mass")), int(input("Fuel mass per dt")))
rocket1.advance() # выполняем один шаг, чтобы написать цикл пока тело не упадет
while(rocket1.y>0): # выполняем шаги мат модели, пока ракета не упала
    print(rocket1.m_fuel)
    rocket1.advance()
pp.plot(rocket1.trajectory_x, rocket1.trajectory_y) # построим график траектории полета ракеты
pp.show() # выведем график траектории
