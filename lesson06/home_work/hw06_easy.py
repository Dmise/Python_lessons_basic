# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle(object):

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.ax = x1
        self.ay = y1
        self.bx = x2
        self.by = y2
        self.cx = x3
        self.cy = y3
        self.a = math.sqrt((self.bx - self.cx) ** 2 + (self.by - self.cy) ** 2)
        self.b = math.sqrt((self.ax - self.cx) ** 2 + (self.ay - self.cy) ** 2)
        self.c = math.sqrt((self.ax - self.bx) ** 2 + (self.ay - self.by) ** 2)

    def area(self):
        triangle_area = math.fabs(
            1 / 2 * ((self.ax - self.cx) * (self.by - self.cy) - (self.ay - self.cy) * (self.bx - self.cx)))
        return triangle_area

    def high(self, letter):
        if letter == 'a':
            return 2 * self.area() / self.a
        elif letter == 'b':
            return 2 * self.area() / self.b
        elif letter == 'c':
            return 2 * self.area() / self.c

    def perimeter(self):
        return self.a + self.b + self.c


myTriangle = Triangle(3, 2, 7, 5, 0, 0)

print(myTriangle.area())
print(myTriangle.high('a'))
print(myTriangle.high('b'))
print(myTriangle.high('c'))
print(myTriangle.perimeter())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector():

    def __init__(self, p1: Point, p2: Point):
        self.x = p1.x - p2.x
        self.y = p1.y - p2.y


def is_kollinear(a: Vector, b: Vector):   # через определитель матрицы
    opredelitel_matrici = a.x*b.y-a.y*b.x
    if opredelitel_matrici == 0:
        return True
    else:
        return False


class Trapecia():

    def __init__(self, p1, p2, p3, p4):  # конструктор
        self.v_a = Vector(p1, p2)
        self.v_b = Vector(p2, p3)
        self.v_c = Vector(p3, p4)
        self.v_d = Vector(p4, p1)
        self.a = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
        self.b = math.sqrt((p3.x - p2.x) ** 2 + (p3.y - p2.y) ** 2)
        self.test = 'Test'
        self.c = math.sqrt((p4.x - p3.x) ** 2 + (p4.y - p3.y) ** 2)
        self.d = math.sqrt((p1.x - p4.x) ** 2 + (p1.y - p4.y) ** 2)
        self.perimeter = self.a + self.b + self.c + self.d
        _p = self.perimeter / 2  # полупериметр, как локальная переменная
        self.area = math.sqrt(_p * (_p - self.a) * (_p - self.b) * (_p - self.c))  # формула Герона

    def is_iso_trapecia(self):  # является ли фигура равнобедренной трапецией
        if is_kollinear(self.v_a, self.v_c):
            if self.b == self.d:
                return True
        if is_kollinear(self.v_b, self.v_d):
            if self.a == self.c:
                return True

        return False

    def area(self):
        return self.area

# Напор точек #1
a = Point(0, 0)
b = Point(1, 3)
c = Point(3, 3)
d = Point(4, 0)
#
# Напор точек #2
a1 = Point(0, 0)
b1 = Point(0, 3)
c1 = Point(3, 3)
d1 = Point(3, 0)

# Напор точек #3
a2 = Point(0, 0)
b2 = Point(1, 3)
c2 = Point(3, 3)
d2 = Point(5, 0)

my_trapecia1 = Trapecia(a, b, c, d) # равнобедренная  трапеция
my_trapecia1 = Trapecia(a1, b1, c1, d1)  # квадрат - равнобедренная
my_trapecia = Trapecia(a2, b2, c2, d2) # НЕ равнобедренная трапеция

print("задача 2")

print(f"Площадь трапеции = {my_trapecia.area}")
print("Длины торон трапеции:")
print(my_trapecia.a)
print(my_trapecia.b)
print(my_trapecia.c)
print(my_trapecia.d)
print(f"Периметр трапеции = {my_trapecia.perimeter}")

print("Является ли данная трапеция равностроннней:")
print(my_trapecia.is_iso_trapecia())

