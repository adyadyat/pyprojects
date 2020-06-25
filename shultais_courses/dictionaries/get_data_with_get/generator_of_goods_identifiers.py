import sys

sizes = {
    "44": "xs",
    "46": "s",
    "48": "m",
    "50": "l",
    "52": "xl"
}

sex = {
    "m": "m",
    "f": "w",
    "w": "w"
}

brand = sys.argv[1]
size = sizes.get(sys.argv[2], "all")
sex1 = sex.get(sys.argv[3], "unisex")
name = brand.lower()
name = name.split()
name.append(size)
name.append(sex1)
name = "-".join(name)
print(name)

"""
# Получаем данные
product = sys.argv[1]
size = sys.argv[2]
sex_param = sys.argv[3]


# Выводим результат.
print("{}-{}-{}".format(
    product.lower().replace(" ", "-"),
    sizes.get(size, "all"),
    sex.get(sex_param, "unisex"),
))

ГЕНЕРАТОР ИДЕНТИФИКАТОРОВ ТОВАРОВ
В редакторе ниже два словаря: один отвечает за размеры одежды, 
а второй за пол, для которого предназначена одежда. 
Нужно написать программу, 
которая будет генерировать идентификаторы товаров.

Программа должна принимать 
из аргументов командной строки три параметра: 
название товара, размер и пол. 
Далее она должна выводить строку следующего вида: 
название-размер-пол.

При этом название нужно привести к нижнему регистру 
и заменить все пробелы на черточки.
Размер нужно взять из словаря sizes, 
если в нем нет передаваемого размера, но надо подставить all.
Пол нужно взять из словаря sex, если пола в словаре нет, 
то нужно вывести unisex.

Пример использования

> python program.py 'Nike T-Shirt' '44' 'm'
> nike-t-shirt-xs-m

> python program.py 'Adidas Original Superstar' '' ''
> adidas-original-superstar-all-unisex
"""