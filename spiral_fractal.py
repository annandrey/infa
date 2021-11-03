import turtle as tl
def draw_fractal(sp_rad):
    """"
   Функция рисует "золотую спираль" заданного размера
   sp_rad:
      длина стороны первого куба спирали
    """
    while sp_rad>0:
        for _ in range (4):
            tl.fd(sp_rad)
            tl.lt(90)
        tl.color("blue")
        tl.circle(sp_rad, 90)
        sp_rad /= 1.6
        tl.color("black")
tl.shape("turtle")
sp_size = int(input("Введите n"))
draw_fractal(sp_size)
tl.done()
