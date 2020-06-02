import sys

# Получаем все цены и разбиваем их по пробелу.
prices = sys.argv[1].strip().split()

# Присваиваем каждой переменной своё значение,
# предварительно преобразовав его к целому числу.
bread = int(prices[0])
milk = int(prices[1])
eggs = int(prices[2])
avg = int((bread + milk + eggs) / 3)
# Считаем среднее и выводим результат.
print(avg)