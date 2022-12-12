# Найти номер четверти, в которой находится точка с координатами x, y
def GetQuarter(x, y):
    if x > 0 and y > 0: return 1
    if x < 0 and y > 0: return 2
    if x < 0 and y < 0: return 3
    if x > 0 and y < 0: return 4


print("Поиск номера четверти плоскости, в которой находится точка с указанными координатами.")
inp = input("Введите координаты точки в формате: X,Y\n")
try:
    dots = inp.split(',')
    if len(dots) != 2: raise ValueError
    x = int(dots[0])
    y = int(dots[1])
    if x == 0 or y == 0: raise ValueError
    quarter = GetQuarter(x, y)
    print("Точка ноходится в четверти {}".format(quarter))
except:
    print("Неправильный формат ввода данных")