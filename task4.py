# Получить диапазон координат точек для четверти quarter
def GetRange(quarter):
    if quarter == 1: return "X > 0 - Y > 0"
    if quarter == 2: return "X < 0 - Y > 0"
    if quarter == 3: return "X < 0 - Y < 0"
    if quarter == 4: return "X > 0 - Y < 0"


print("Поиск диапазона возможных координат точек по заданному номеру четверти.")
inp = input("Введите номер четверти...\n")
try:
    quarter = int(inp)
    if quarter < 1 or quarter > 4: raise ValueError
    range = GetRange(quarter)
    print("Диапазон координат точек для четверти {0}: {1}".format(quarter, range))
except:
    print("Неправильный формат ввода данных")