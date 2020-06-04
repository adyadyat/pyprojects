import sys
num = sys.argv[1] # +7-111-222-33-44
num = num.replace("+7-", "+7 (").replace("-", ") ", 1)
print(num) # +7 (111) 222-33-44

# Альтернативный вариант
# num = num.replace("-", " (", 1).replace("-", ") ", 1)