import sys
word = sys.argv[1]
w = (len(word) - 1) // 2 # Средняя буква если нечетное, если нет, то слева от центра
print(word[0], word[-1])
print(word[w]) # вывод буквы средней или левее от середины