
products_file = open("shoping_list.txt", encoding="utf8")
products = products_file.read().strip()
print(products)

#products_file = open("shoping_list.txt", "a", encoding="utf8")
#products_file.write("\nМолоко")