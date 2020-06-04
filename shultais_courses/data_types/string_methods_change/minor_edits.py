import sys
num = sys.argv[1]
num = num[0:7].replace("-", " ") + num[7:]
print(num)
# +7-111-222-33-44
# Альтернативный вариант
# num = num.replace("-", " ", 2)