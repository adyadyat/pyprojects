import sys

key = sys.argv[1]

rainbow = {
	"red": "красный",
	"orange": "оранжевый",
	"yellow": "желтый",
	"green": "зеленый",
	"blue": "голубой",
	"indigo": "синий",
	"violet": "фиолетовый"
}

print(rainbow[key])

"""
ДОСТУП ПО КЛЮЧУ
Используя словарь из прошлой задачи, 
напишите программу, 
которая получает первым аргументом 
командной строки название ключа словаря, 
а затем выводит значение связанное с этим ключом.

Пример использования:
> python program.py red
> красный
"""