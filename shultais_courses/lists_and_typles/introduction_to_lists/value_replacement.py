import sys

index_lang = int(sys.argv[1])
lang = sys.argv[2]
languages = ['Python', 'C++', 'JavaScript', 'Java']
languages[index_lang] = lang

print(languages)

"""
ЗАМЕНА ЗНАЧЕНИЯ
Напишите программу, 
которая принимает из аргументов командной строки индекс 
элемента списка languages, а также новое значение, 
которое должно быть размещено на позиции переданного индекса. 
После замены элемента, программа должна вывести список в консоль.

Пример использования:
> python program.py 1 PHP
> ['Python', 'PHP', 'JavaScript', 'Java']
"""