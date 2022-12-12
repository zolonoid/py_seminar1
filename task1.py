days = ("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
print("Проверка выходного дня")
inp = input("Введите цифру дня недели...\n")
try:
    num = int(inp)
    if num < 1 or num > 7: raise ValueError
    print("{0} -{1}выходной день".format(days[num-1]," " if num > 5 else " не "))
except:
    print("Это не день недели")