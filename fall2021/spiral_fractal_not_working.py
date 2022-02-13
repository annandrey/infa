import turtle as tl
def draw_fractal(n):
    tl.screensize(200, 200)
    for i in range (n-2):
        f = 1
        f_p = 1
        a_box = f
        f += f_p
        f_p = a_box
        for i in range (4):
            tl.fd(f)
            tl.lt(90)
    tl.circle(f, 90)
tl.shape("turtle")
n = int(input("Введите n"))
draw_fractal(n)
tl.done()
