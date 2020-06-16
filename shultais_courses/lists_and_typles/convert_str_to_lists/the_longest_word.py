import sys

words = sys.argv[1]

words = words.split()
words = sorted(words, key=len, reverse=True)

print(words[0])

"""
import sys

text = sys.argv[1]

# Разбиваем в список.
words = text.split()

# Сортирвем список по длине слова.
words.sort(key=len)

# Выводим самое последнее слово.
print(words[-1])

САМОЕ ДЛИННОЕ СЛОВО
Напишите программу, 
которая первым аргументом командной строки 
принимает строку со списком слов, разделенных пробелом, 
а после выводит самое длинное из этих слов.

Пример использования:
> python program.py 'кошки собаки пингвины зебры'
> пингвины
"""