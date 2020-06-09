lang_file = open("language.txt", encoding="cp1251")
lang = lang_file.read()
print(lang)

"""
ЯЗЫК
Рядом с программой находится файл language.txt, в котором содержится текст в кодировке cp1251.
Напишите программу, которая читает файл и выводит его содержимое.

Пример использования в командной строке Windows:
> python program.py
> English
"""