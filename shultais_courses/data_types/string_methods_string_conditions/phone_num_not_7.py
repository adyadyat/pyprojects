import sys

num = sys.argv[1]
num = num.startswith("+7")
print(not num)

# ТЕЛЕФОННЫЙ НОМЕР НЕ НА +7
"""
Если перед переменной, 
которая содержит логическое значение поставить слово not,
 то значение переменной будет изменено на обратное.

# Создаем переменную is_phone, содержащую логическое значение True.
is_phone = True

# Выводим оригинальное значение.
print(is_phone)
True

# Выводим обратное значение.
print(not is_phone)
False
Напишите программу, 
которая первым аргументом командной строки принимает телефонный номер,
а после выводит True если номер не начинается на +7 и False
если начинается с +7.
"""