import sys

budget = [
    [176, 148, 245, 378, 451, 568, 135,
     146, 761, 414, 135, 171],  # 2019
    [211, 175, 301, 474, 569, 721, 158,
     172, 972, 521, 158, 205],  # 2020
    [257, 210, 374, 599, 722, 920, 188,
     206, 1246, 660, 188, 249]  # 2021
]

year = int(sys.argv[1]) - 2019
month = int(sys.argv[2]) - 1
change = int(sys.argv[3])

budget[year][month] = change
result = sum(budget[year]) * 1000
print("{:,}".format(result).replace(",", " "))

"""
import sys

budget = [
    [176, 148, 245, 378, 451, 568, 135, 146, 761, 414, 135, 171],  # 2019
    [211, 175, 301, 474, 569, 721, 158, 172, 972, 521, 158, 205],  # 2020
    [257, 210, 374, 599, 722, 920, 188, 206, 1246, 660, 188, 249]  # 2021
]

# Задаем начальный год.
start_year = 2019

# Получаем индекс для года.
year = int(sys.argv[1])
year_index = year - start_year

# Получаем индекс для месяца.
month_index = int(sys.argv[2]) - 1

# Получаем новое значение.
new_budget = int(sys.argv[3])

# Вносим изменение.
budget[year_index][month_index] = new_budget

# Получем реальный бюджет.
year_budget = sum(budget[year_index]) * 1000

# Выводим результат.
print("{0:,}".format(year_budget).replace(",", " "))

ПРАВИМ БЮДЖЕТ
Ниже содержится список budget с бюджетами компании по годам и месяцам. Основная последовательность отвечает за годы, а вложенные списки за месяцы конкретного года, начиная с 2019.

Бюджет компании записывается в тысячах, то есть значение 176 означает 176 000 рублей.

Напишите программу, которая принимает из аргументов командной строки три параметра: год, номер месяца (1 - январь и т.д.), а также новое значение для этого месяца.

После программа должна внести изменение в список, а затем посчитать и вывести размер годового бюджета. При этом данные нужно вывести в полном формате (не в тысячах) с разбивкой числа на разряды.

Пример использования:
> python program.py 2019 1 276
> 3 828 000
"""