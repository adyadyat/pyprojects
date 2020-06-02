import sys
x1 = int(sys.argv[1])
y1 = int(sys.argv[2])
x2 = int(sys.argv[3])
y2 = int(sys.argv[4])
root = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
print(root)
# Расстояние между точками
"""
Чтобы получить квадратный корень из числа,
надо возвести его в степень 0.5:
print(16 ** 0.5)
4.0
"""