d = {
	"name": "Название 1",
	"Name": "Название 2",
#	"name": "Название 3",
	"1": "1",
	1: 1,
	1.0: 1.0,
	1.01: 1.01,
	0: 0,
	False: False,
	True: True,
	None: None
}

print(d)

state = {
	False: "Отсутствует",
	True: "В списке",
}

products = [17, 57, 1, 59, 85, 15, 22]
#in_products = 17 in products
in_products = products.count(17)

print(in_products)
print(state[in_products])