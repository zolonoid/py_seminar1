import re
import math


# Получить координаты точки из строки
def GetCoordinates(dot):
    m = re.match("[A-Z]\((-?\d+),(-?\d+)\)", dot)
    x = int(m.group(1))
    y = int(m.group(2))
    return (x, y)


# Найти расстояние между точками
def GetDistance(ax, ay, bx, by):
    xd = abs(ax - bx)
    yd = abs(ay - by)
    return math.sqrt((xd**2 + yd**2))


print("Расстояние между двумя точками в 2D пространстве.")
inp = input("Введите координаты точек в формате A(x,y);B(x,y)\n")
try:
    dots = inp.split(';')
    if len(dots) != 2: raise ValueError
    ax, ay = GetCoordinates(dots[0])
    bx, by = GetCoordinates(dots[1])
    dist = GetDistance(ax, ay, bx, by)
    print("Расстояние между точками: {}".format(dist))
except:
    print("Неправильный формат ввода данных")
