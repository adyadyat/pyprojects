import sys

year = int(sys.argv[1])

populations_file = open("populations.txt")
populations = populations_file.readlines()
year_file = populations[0].strip()
index = year - int(year_file)
populations = populations[1:]
print(populations[index])

"""
import sys

# Открываем файл
population_file = open("population.txt")

# Сохраняем данные в список.
all_data = population_file.readlines()

# Получаем начальный год.
start_year = int(all_data[0])

# Вычисляем список населения.
population = all_data[1:]

# Получаем год.
year = int(sys.argv[1])

# Приводим к индексам списка.
index = year - start_year

# Выводим результат.
print(population[index].strip())

НАСЕЛЕНИЕ, ЧАСТЬ 3
Рядом с программой находится файл population.txt с населением 
России за разные годы. В первой строке содержится год, 
с которого начали заполнять этот файл. 
В следующих строках хранятся непосредственно данные 
о населении — каждое значение с новой строки и каждое 
отвечает за определенный год.

Например, в следующем файле первая строка содержит год — 2004, 
соответственно население 144168205 относится к 2004 году, 
143474219 к 2005 и тд.

2004
144168205
143474219
142753551
Напишите программу, которая принимает 
из аргументов командной строки год, 
а затем выводит население этого года.

Пример использования:
> python program.py 2006
> 142753551
"""