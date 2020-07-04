user = {
	"name": {"first": "Антон"},
	"price": [3000, "руб"],
	"sale": .3
}
"""
user = {
	"first_name": "Антон",
	"price": 3000,
	"sale": .3
}

hello_template = "Здравствуйте, {}!\n" \
					"Стоимость товара: {} руб.\n" \
					"Ваша скидка: {}."

print(hello_template.format(
	user["first_name"],
	user["price"],
	user["sale"]
))

hello_template = "Здравствуйте, {u[first_name]}!\n" \
					"Стоимость товара: {u[price]} руб.\n" \
					"Ваша скидка: {u[sale]:.0%}."

print(hello_template.format(u=user))
"""
hello_template = "Здравствуйте, {name[first]}!\n" \
					"Стоимость товара: {price[0]} {price[1]}.\n" \
					"Ваша скидка: {sale:.0%}."

print(hello_template.format(**user))