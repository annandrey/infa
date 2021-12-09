
class Deduction:
    def __init__(self, numb, base, res):
        """
       Опишем класс кольца вычетов по модулю
       Параметры:
       numb:
          число, которое будем рассматривать в кольце
       base:
          основание кольца вычетов
       res:
          остаток от деления numb и base
       """
        self.numb = numb
        self.base = base
        self.res = res
    def great_common(self):
        """
        Функция для поиска остатка от деления
        """
        while self.numb>self.base:
            self.res = self.numb - self.base
        return self.res
    def __add__(self, other):
        """
       Функция для сложения
       """
        return(self.num + other.num)%self.base
    def __sub__(self, other):
        """
        Функция для вычитания
        """
        ded = self.num - other.num
        if ded<0:
            ded += self.base
    def __mul__(self, other):
        """
        Функция для умножения
        """
        return(self.num * other.num)%self.base
    def __div__(self, other):
        """
        Функция для деления
        """
        if other.num == 0:
            raise ZeroDivisionError
        if self.num % other.num!=0:
            raise RuntimeError
        return self.num / other.num
    def __str__(self):
        """
        Функция для преобразования числа в строку
        """
        return str(self)
