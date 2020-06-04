import sys
# Ввод двух параметров 'Введение в курс' 7
# Вывод не менее 40 сим.строки Введение в курс ...................... 7
chapter = sys.argv[1]
page = sys.argv[2]

# Мой вариант с применением метода S.center()
S = chapter + str(page)
count = 40 - len(S)
S1 = "." * (count - 2)
S1 = S1.center(count)
print(chapter + S1 + str(page))

# Альтернативный вариант от преподавателя
# Формируем строку точек
dots = "." * (40 - (len(chapter) + len(page)) - 2)

# Выводим главу, точки и страницу.
print(chapter, dots, page)