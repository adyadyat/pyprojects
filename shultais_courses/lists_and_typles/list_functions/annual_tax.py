import sys

annual = int(sys.argv[1]) / 100

revenue = [178, 351, 145, 764, 514, 456,
           411, 145, 275, 245, 441, 716]

result = sum(revenue) * annual

print("{:.2f}".format(result))

"""
import sys

revenue = [178, 351, 145, 764, 514, 456,
           411, 145, 275, 245, 441, 716]


# Получаем процент налога.
tax = int(sys.argv[1])

# Вычисляем величину налога.
tax = sum(revenue) / 100 * tax

# Выводим результат.
print("{:.2f}".format(tax))

ГОДОВОЙ НАЛОГ
Ниже содержится список revenue с доходами компании за год. 
Напишите программу, 
которая принимает первым аргументом 
командной строки размер налога в процентах, 
а после рассчитывает и выводит величину налога, 
который компания должна заплатить за год.

Размер налога нужно вывести с двумя знаками после запятой.

Пример использования:
> python program.py 6
> 278.46
"""