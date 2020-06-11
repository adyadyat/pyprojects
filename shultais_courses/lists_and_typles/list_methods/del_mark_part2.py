import sys

d = sys.argv[1].strip()

marks = ["BMW", "Toyota", "Mercedes", "Lada", "Nissan", "Audi"]

marks.remove(d)

print(marks)

"""
УДАЛЯЕМ МАРКУ, ЧАСТЬ 2
В программе ниже создан список с марками автомобилей. 
Расширьте код так, чтобы программа принимала из 
первого аргумента командной строки название марки, 
а затем удаляла её из списка.

Пример использования:
> python program.py Toyota
> ['BMW', 'Mercedes', 'Lada', 'Nissan', 'Audi']
"""