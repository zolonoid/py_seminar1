print("Проверка истинности утверждения ¬(X ∨ Y ∨ Z) = ¬X ∧ ¬Y ∧ ¬Z")
for x in (False, True):
    for y in (False, True):
        for z in (False, True):
            result = "Да" if not(x or y or z) == (not x and not y and not z) else "Нет"
            print("¬({0} ∨ {1} ∨ {2}) = ¬{0} ∧ ¬{1} ∧ ¬{2}  -  {3}".format(x, y, z, result))
