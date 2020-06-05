import sys
rub = sys.argv[1]
only_rub = rub.find(".") # поиск точки
print(rub[0:only_rub]) # вывод среза целого числа 
# print(amount[:dot])
