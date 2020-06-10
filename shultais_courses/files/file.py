
#products_file = open("shoping_list.txt", encoding="utf8")
#products = products_file.read().strip()
#
#products_file = open("shoping_list.txt", "a", encoding="utf8")
#products_file.write("\nМолоко")


products_file = open("shoping_list.txt", encoding="utf8")
products = products_file.read().strip()
products = products.replace("масло\n", "").title()
products_file.close()

new_products_file = open("new_shopping_list.txt", "w")
new_products_file.write(products)
new_products_file.close()

# "r+" режим чтения и дозаписи