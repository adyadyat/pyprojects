import sys
hidden_phone_num = sys.argv[1]
hidden_num = hidden_phone_num[0:5] + ("?" * 5) + hidden_phone_num[-2:]
print(hidden_num)

# +7707?????66 Скрытие тел номера