import sys

# Получаем данные.
model = sys.argv[1]
new_price = int(sys.argv[2])
new_count = int(sys.argv[3])

# Исходный словарь.
product = {
    "model": "UE43NU7097U",
    "brand": "Samsung",
    "price": 27990,
    "count": 7
}

# Обновляем данные.
product["count"] = new_count
product.update(model=model, price=new_price)
# product.update(model=model, price=new_price, count=new_count)
# Выводим результат.
print(product)

"""
ЧИНИМ ПРОГРАММУ
Начинающий разработчик написал программу, 
которая принимает из аргументов командной строки модель, 
новую цену и новое количество товара, 
а затем меняет эти данные в словаре product. 
Но программа не работает, исправьте в ней все ошибки.

Пример использования:
> python program.py UE32M5550AU 23990 3
> {'model': 'UE32M5550AU', 'brand': 'Samsung', 'price': 23990, 'count': 3}
"""