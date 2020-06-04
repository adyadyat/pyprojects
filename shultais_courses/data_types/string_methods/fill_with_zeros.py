import sys

digit1 = sys.argv[1]
digit2 = sys.argv[2]
digit3 = sys.argv[3]
# Выравнивание по правому краю
print(digit1.zfill(15))
print(digit2.zfill(15))
print(digit3.zfill(15))
# S.zfill(width)
# Делает длину строки не меньшей width, 
# по необходимости заполняя первые символы нулями
# 000000000000012
# 000000000000543
# 000000000000123