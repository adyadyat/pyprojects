from datetime import date
today = date.today()

data = ["ОЛ-17.12", 12_000, today]
# 1 вариант
#product_template = "Счет: {}\n" \
#					"Сумма: {} руб.\n" \
#					"Дата: {}"

#print(product_template.format(data[0], data[1], data[2]))
# 2 вариант
#product_template = "Счет: {d[0]}\n" \
#					"Сумма: {d[1]} руб.\n" \
#					"Дата: {d[2]:%d.%m.%Y}"

#print(product_template.format(d=data))
# 3 вариант
product_template = "Счет: {0}\n" \
					"Сумма: {1} руб.\n" \
					"Дата: {2:%d.%m.%Y}"

print(product_template.format(*data))