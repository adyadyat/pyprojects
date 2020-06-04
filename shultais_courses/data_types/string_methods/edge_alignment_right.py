import sys

digit1 = sys.argv[1]
digit2 = sys.argv[2]
digit3 = sys.argv[3]
# Выравнивание по правому краю
print(digit1.rjust(15, "."))
print(digit2.rjust(15, "."))
print(digit3.rjust(15, "."))
# S.rjust(width, fillchar=" ")
# Делает длину строки не меньшей width, 
# по необходимости заполняя первые символы символом fillchar
# 5 115 1115
# .............15
# ............115
# ...........1115