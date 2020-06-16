import sys

year = int(sys.argv[1]) - 2003

populations_file = open("populations.txt")
populations = populations_file.readlines()
print(populations[year].strip("\n"))

"""
import sys

# Открываем файл
population_file = open("population.txt")

# Сохраняем данные в список.
population = population_file.readlines()

# Получаем год.
year = int(sys.argv[1])

# Приводим к индексам списка.
index = year - 2003

# Выводим результат.
print(population[index].strip())

НАСЕЛЕНИЕ, ЧАСТЬ 2
Рядом с программой находится файл population.txt, 
в каждой строке которого хранится население России, 
начиная с 2003 года. То есть в первой строке население 2003 года, 
во второй 2004 и тд.

Напишите программу, 
которая принимает из аргументов командной строки год, 
а затем выводит население этого года.

Пример использования:
> python program.py 2006
> 142753551
"""