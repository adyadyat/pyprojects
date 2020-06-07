import sys

f_name = sys.argv[2]
l_name = sys.argv[1]
year = int(sys.argv[3])
l_name_f = "| {:<8s} |".format(l_name)
f_name_f = "{:<8s} |".format(f_name)
year_f = "{:>6d} |".format(year)
print(l_name_f, f_name_f, year_f)
"""
import sys

text1 = sys.argv[1]
text2 = sys.argv[2]
text3 = sys.argv[3]

print("| {:<8s} | {:<8s} | {:>6s} |".format(text1, text2, text3))
ВЫРАВНИВАНИЕ ПО ПРАВОМУ КРАЮ, ЧАСТЬ 4
Для выравнивания текста по правому краю используется 
следующий спецификатор: {:>Ns}, где N общая длина строки, 
которая должна получиться.

Перепишите предыдущую задачу так, 
чтобы последний параметр был длиной в 6 символов и 
выравнен по правому краю.

Пример использования в командной строке Windows:
> python program.py Иванов Иван 1994
> | Иванов   | Иван     |   1994 |
"""