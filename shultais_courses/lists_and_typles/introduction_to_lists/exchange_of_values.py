import sys

languages = ['Python', 'C++', 'JavaScript', 'Java']
lang = languages[int(sys.argv[1])]
languages[int(sys.argv[1])] = languages[int(sys.argv[2])]
languages[int(sys.argv[2])] = lang

print(languages)

"""
import sys

index1 = int(sys.argv[1])
index2 = int(sys.argv[2])

languages = ['Python', 'C++', 'JavaScript', 'Java']

# Простой алгоритм
temp = languages[index1]
languages[index1] = languages[index2]
languages[index2] = temp

# Альтернативный вариант: обмен в одно действие
languages[index1], languages[index2] = languages[index2], languages[index1]

print(languages)

ОБМЕН ЗНАЧЕНИЙ
Напишите программу, 
которая принимает из аргументов командной строки два числа, 
а затем меняет в списке languages значения, 
которые находятся на индексах, соответствующих переданным числам.

Пример использования:
> python program.py 0 1
> ['C++', 'Python', 'JavaScript', 'Java']
"""