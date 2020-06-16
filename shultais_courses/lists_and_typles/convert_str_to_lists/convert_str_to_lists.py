phone = "89513658483"
full_name = "Иванов Андрей Петрович"
ip = "127.0.0.1"

phone_list = list(phone)
print(phone_list) # ['8', '9', '5', '1', '3', '6', '5', '8', '4', '8', '3']


fio = full_name.split()
print(fio) # ['Иванов', 'Андрей', 'Петрович']

ip = ip.split(".")
print(ip) # ['127', '0', '0', '1']

last_name, first_name, patronymic = full_name.split()[:2]
print(last_name) # Иванов
print(first_name) # Андрей
# print(patronymic) # Петрович