products_file = open("products.txt", encoding="cp1251")
products = products_file.read()

products_file_w = open("products.txt", "w", encoding="utf8")
products_file_w.write(products)
products_file_w.close()

"""
# Открываем файл на чтение в кодировке cp-1251.
products_file = open("products.txt", "r", encoding="cp1251")

# Читаем данные.
products = products_file.read()

# Закрываем файл.
products_file.close()

# Открыаем файл на запись в кодировке utf-8
products_file = open("products.txt", "w")

# Записываем в файл.
products_file.write(products)

# Закрываем файл
products_file.close()

ПЕРЕКОДИРУЕМ ФАЙЛ
Рядом с программой находится файл products.txt в кодировке cp1251.
Напишите программу, которая перекодирует его в кодировку utf-8.

После того как программа выполнится, 
система сама откроет файл products.txt и проверит его содержимое.
"""