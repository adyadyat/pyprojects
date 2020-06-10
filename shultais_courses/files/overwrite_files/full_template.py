import sys
name = sys.argv[1]
template_file = open("template.txt")
template = template_file.read()
template = template.replace("{{ name }}", name)
template_file.close()

new_temtale = open("template.txt", "w")
new_temtale.write(template)
new_temtale.close()
"""
import sys

# Получаем имя.
name = sys.argv[1].strip()

# Открываем файл на чтение.
template_file = open("template.txt", "r")

# Читаем данные.
template = template_file.read()

# Делаем замену.
text = template.replace("{{ name }}", name)

# Закрываем файл.
template_file.close()

# Открываем файл на запись.
template_file = open("template.txt", "w")

# Записываем данные.
template_file.write(text)

# Закрыавем файл
template_file.close()

ЗАПОЛНЯЕМ ШАБЛОН
Рядом с программой находится файл template.txt, 
в котором хранится шаблон текста.
В шаблоне есть текст вида {{ name }}, 
который нужно заменить на реальное имя пользователя.

Напишите программу, 
которая принимает из первого аргумента командной строки имя пользователя, 
а затем подставляет его в шаблон и записывает результат в файл.

После того как программа выполнится, 
система сама откроет файл template.txt и проверит его содержимое.
"""


