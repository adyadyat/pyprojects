import sys

num = []
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
num4 = int(sys.argv[4])
num5 = int(sys.argv[5])
num += [num1]
num += [num2]
num += [num3]
num += [num4]
num += [num5]
print(max(num))

"""
# Вариант 1
import sys
numbers = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), 
           int(sys.argv[4]), int(sys.argv[5])]

# Получаем максимальное значение с помощью функции max
print(max(numbers))

# Вариант 2
# Создаем список из аргументов командной строки.
# Каждый аргумент предварительно преобразовываем к целому числу.
import sys
numbers = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), 
           int(sys.argv[4]), int(sys.argv[5])]

# Сортируем список
numbers.sort()

# Выводим последний элемент
# После сортировки там как раз будет самое большое число.
print(numbers[-1])



# Вариант 3 (продвинутый)
import sys

# Решение в одну строку с помощью функционального программирования (ФП)
# Если вам интересно как это работает, 
# то у нас есть отдельный мини-курс по ФП на Python 3
print(max(map(int, sys.argv[1:6])))

САМОЕ БОЛЬШОЕ ЧИСЛО
Напишите программу, 
которая получает пять чисел из аргументов командной строки, 
а затем выводит самое большое из них.

Пример использования:
> python program.py 2 42 3 56 4
> 56
"""