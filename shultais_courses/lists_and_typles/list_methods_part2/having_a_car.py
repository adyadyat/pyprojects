import sys

car = "{} {}".format(sys.argv[1], sys.argv[2])

cars = ["Ford Focus", "Skoda Octavia", "Toyota Prius",
        "Hyundai Solaris", "Volkswagen Polo", "Skoda Rapid"]

print(car in cars)

"""
import sys

cars = ["Ford Focus", "Skoda Octavia", "Toyota Prius",
        "Hyundai Solaris", "Volkswagen Polo", "Skoda Rapid"]

# Получаем марку и модель.
mark = sys.argv[1]
model = sys.argv[2]

# Склеиваем.
value = "{} {}".format(mark, model)

# Проверяем и выводим результат.
print(value in cars)

НАЛИЧИЕ АВТОМОБИЛЯ
Ниже в редакторе содержится список cars с автомобилями. 
Напишите программу, 
которая принимает из аргументов командной строки два параметра: 
марку и модель автомобиля, 
а затем выводит True если автомобиль есть в списке и False 
в противном случае.

Пример использования:
> python program.py Ford Focus
> True
"""