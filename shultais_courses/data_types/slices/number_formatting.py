import sys
num_format = sys.argv[1]
num = "+7 (" + num_format[1:4] + ") " + num_format[4:7] + "-" +num_format[7:9] + "-" + num_format[-2:]
print(num)

# +7 (707) 988-98-66 Форматирование номера