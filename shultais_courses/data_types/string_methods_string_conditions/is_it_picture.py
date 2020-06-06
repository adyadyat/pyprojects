import sys

picture = sys.argv[1]
png = picture.lower().endswith(".png")
jpg = picture.lower().endswith(".jpg")
jpeg = picture.lower().endswith(".jpeg")
gif = picture.lower().endswith(".gif")
print(png or jpg or jpeg or gif)

"""
ЭТО ИЗОБРАЖЕНИЕ?
Введение
Мы уже познакомились с логическим типом, а также с оператором not, 
который меняет логическое значение на обратное. 
Давайте теперь изучим логическую операцию or.

Логическая операция or сравнивает несколько значений и возвращает True, 
если хотя бы одно из них будет логически верным:

# Создаем четыре логические переменные.
is_male = True
is_female = False
is_old = True
is_young = False

# Сравниваем: True или False.
# Получаем True, так как одна из переменных True.
print(is_male or is_female)
True

# Сравниваем: False или True (поменяли местами).
# Всё равно получаем True, так как одна из переменных True.
print(is_female or s_male)
True

# Сравниваем: False или False.
# Получаем False, так как нет True.
print(is_young or is_female)
False

# Сравниваем все переменные.
print(is_young or is_female or is_old or is_young)
True

Задание
Напишите программу, которая первым аргументом командной строки принимает 
название файла, а после выводит True если это изображение, 
и False в противном случае.
Определять изображение это или нет нужно 
по расширению файла: png, jpeg, jpg или gif.
Учитывайте, что имя может быть набрано в разных регистрах.
> python program.py photo.png
> True
> python program.py photo.jpg
> True
> python program.py ROOM.PNG
> True
> python program.py video.mp4
> False
"""