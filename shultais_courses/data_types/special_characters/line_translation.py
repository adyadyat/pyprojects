import sys

br = sys.argv[1]
border1 = br.replace("<br>", "\n")
print(border1)
"""
import sys

text = sys.argv[1]

# Очищаем строку и заменяем <br> на переносы строки.
text = text.strip().replace("<br>", "\n")

# Выводим текст.
print(text)

ПЕРЕВОД СТРОКИ
Для перевода строк в HTML служит тег <br>. Напишите программу, 
которая первым аргументом командной строки принимает HTML-текст, 
а затем преобразовывает <br>-теги к переводам строк на 
Python и выводит результат.

Пример использования:
> python title.py 'Leading growth:<br>why strategy matters'
> Leading growth:
> why strategy matters
"""