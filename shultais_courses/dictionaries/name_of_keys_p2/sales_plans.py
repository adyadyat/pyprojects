import sys

plans = {
    2017: [False, False, False, False, False, False, False, False, False, False, False, False],
    2018: [True, True, False, False, True, False, True, True, False, True, True, True],
    2019: [True, True, True, True, True, False, True, True, False, True, True, True],
    2020: [True, True, True, True, True, False, True, True, False, False, False, False],
    2021: [True, True, True, True, True, True, True, True, True, True, True, True]
}

year = int(sys.argv[1])
in_plans = plans[year]
in_plans = in_plans.count(True)
in_plans = in_plans * 100 / 12

print("{:.0f}%".format(in_plans))

"""
# Вычисляем процент.
# Так как True - это синоним 1, 
то можно прсото сложить все значения списка.
percent = sum(plans[year]) * 100 / 12

# Выводим результат.
print("{:.0f}%".format(percent))

ПЛАН ПО ПРОДАЖАМ
В редакторе ниже находится словарь plans, 
который содержит данные о выполнение ежемесячных планов по продажам. 
Ключом словаря является год, а значение — это список из 12 элементов, 
по элементу на каждый месяц. True означает, 
что план в текущем месяце выполнен, а False, что нет.

Напишите программу, 
которая первым аргументом командной строки получает год, 
а затем выводит процент выполнения планов в этом году.

Данные нужно округлить и добавить к ним символ процента.

Пример использования:
> python program.py 2018
> 67%

"""