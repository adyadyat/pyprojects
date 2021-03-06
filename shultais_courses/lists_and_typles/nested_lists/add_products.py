import sys

products = [
    ["молоко", "кефир"],  # молочка
    ["котлеты", "курица", "говядина"]  # мясо
]

index = int(sys.argv[1])
new_products = sys.argv[2:]

products[index] = products[index] + new_products
# Расширяем список новыми продуктами.
#products[index].extend(new_products)

print(products)

"""
ДОБАВЛЯЕМ ПРОДУКТЫ
Ниже содержится список products с товарами разбитыми по категориям. 
Каждая категория товаров помещена в отдельный вложенный список.

Напишите программу, 
которая принимает из аргументов командной строки данные в следующем виде: 
первым аргументом идет индекс категории в списке products, 
а далее следует список товаров. 
Программа должна расширить вложенный список, 
который находится по переданному индексу, товарами, 
которые размещены в остальных аргументах. 
В конце нужно вывести получившийся список.

Пример использования:
Товары "свинина" и "телятина" попадают в список, 
который находится на первой по индексу позиции.

> python program.py 1 свинина телятина
> [['молоко', 'кефир'], ['котлеты', 'курица', 'говядина', 'свинина', 'телятина']]
"""