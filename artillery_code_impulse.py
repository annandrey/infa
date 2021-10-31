from matplotlib import pyplot as pp

MODEL_G = 9.81
MODEL_DT = 0.1
class Body:
    def __init__(self, x, y, v_x, v_y):
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
    def __init__(self, x, y, m_body = 250, m_fuel = 1000, d_m = 100, vel_of_exh = 400):
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
        d_m: float
           изменение массы( выброс топлива )
        vel_of_exh:
           скорость струи газа
        """
        super().__init__(x, y, 10, 10) # Вызовем конструктор предка — тела
        self.m_fuel = m_fuel
        self.m_body = m_body
        self.d_m = d_m
        self.vel_of_exh = vel_of_exh
    def advance(self):
        """
        Выполним шаг математической модели ракеты
        """
        super().advance() # вызовем метод предка — тела, т.к. и он для ракеты актуален.

        if self.m_fuel >= self.d_m * MODEL_DT :
            self.m_fuel -= self.d_m * MODEL_DT # вычтем массу сгоревшего топлива
            d_v = ((self.m_fuel + self.m_body) * MODEL_G * MODEL_DT +
             (self.d_m * self.vel_of_exh))/(self.m_body + self.m_fuel)# найдем изменение скорости
            d_vx = d_v * (self.x/(self.x**2 + self.y**2)) # найдем проекцию скорости на ох
            d_vy = d_v * (self.y/(self.x**2 + self.y**2)) # найдем проекцию скорости на оу
            self.v_x += d_vx # запишем приращение скорости для оси х и у
            self.v_y += d_vy
        elif(self.m_fuel > 0 and self.m_fuel < self.d_m * MODEL_DT):
            self.m_fuel = 0
            d_v = (self.d_m * self.vel_of_exh)/(self.m_body + self.m_fuel) # приращение скорости
            d_vx = d_v * (self.x/(self.x**2 + self.y**2)) # найдем проекцию приращения скорости ох
            d_vy = d_v * (self.y/(self.x**2 + self.y**2)) # найдем проекцию приращения скорости оу
            self.v_x += d_vx
            self.v_y += d_vy
rocket1 = Rocket(0, 0, float(input("Body mass")), float(input("Fuel mass")),
 float(input("Fuel mass per dt")), float(input("Velocity of exhaust")))
rocket1.advance() # выполняем один шаг, чтобы написать цикл пока тело не упадет
while rocket1.y>0: # выполняем шаги мат модели, пока ракета не упала
    print(rocket1.m_fuel)
    rocket1.advance()
pp.plot(rocket1.trajectory_x, rocket1.trajectory_y) # построим график траектории полета ракеты
pp.show() # выведем график траектории
print("Наглядный график движения произвольной ракеты")
rocket2 = Rocket(0, 0)
rocket2.advance() # выполняем один шаг, чтобы написать цикл пока тело не упадет
while rocket2.y>0: # выполняем шаги мат модели, пока ракета не упала
    rocket2.advance()
pp.plot(rocket2.trajectory_x, rocket2.trajectory_y) # построим график траектории полета ракеты
pp.show() # выведем график траектории
