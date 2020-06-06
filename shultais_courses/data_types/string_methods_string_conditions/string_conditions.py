domain1 = "www.yandex.ru"
domain2 = "www.youtube.com"
domain3 = "www.rutracker.org"
domain4 = "yandex.ua"

print(domain1.endswith(".ru"))
print(domain2.endswith(".ru"))
print(domain3.endswith(".ru"))
print(domain4.endswith(".ru"))
print("*" * len(domain4))
print(domain1.startswith("www."))
print(domain2.startswith("www."))
print(domain3.startswith("www."))
print(domain4.startswith("www."))
print("*" * len(domain4))
print(domain1.islower())
print(domain2.islower())
print(domain3.isupper())
print(domain4.isupper())
# МЕТОДЫ СТРОК: СОСТОЯНИЕ СТРОК
# Методы возвращают True Falce
# S.endswith(str) Заканчивается ли строка S шаблоном str
# S.startswith(str) Начинается ли строка S с шаблона str
# S.islower() Состоит ли строка из символов в нижнем регистре
# S.isupper() Состоит ли строка из символов в верхнем регистре