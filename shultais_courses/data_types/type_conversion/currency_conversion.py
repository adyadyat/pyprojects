import sys

rate = sys.argv[1] # курс доллара
amount = int(sys.argv[2]) # количество долларов
rate = float(rate.replace(",", "."))

print(amount, "долларов в рублях =", rate * amount, "руб.")
"""
ПРЕОБРАЗОВАНИЕ ВАЛЮТ
Напишите программу, которая принимает из аргументов командной строки два параметра: курс доллара и количество долларов, а затем выводит следующую фразу: «N долларов в рублях = M руб.», где N — это количество долларов, а M — количество рублей по текущему курсу.
Склонением существительных в этой задаче можно пренебречь.

Обратите внимание, что курс доллара передается с запятой в качестве разделителя (64,66), однако в Python к вещественным числам можно преобразовывать только строки с точкой (64.66).
Также учитывайте, что количество долларов является целым числом.

Пример использования:
> python program.py 64,66 12
> 12 долларов в рублях = 775.92 руб.

import sys

# Делаем замену запятой на точку.
rate = sys.argv[1].replace(",", ".")
dollars = sys.argv[2]

# Приводим все данные к числам.
rate = float(rate)
dollars = int(dollars)

# Считаем
full = dollars * rate

# Выводим результат.
print(str(dollars) + " долларов в рублях = " + str(full) + " руб.")
"""