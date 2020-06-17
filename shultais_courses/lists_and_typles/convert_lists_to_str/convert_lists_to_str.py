products = ["молоко", "масло", "сметана", "сливки", "кефир", "сыр"]
name = "продукты"
name = list(name) # ["продукты"]
name[0] = "П" # ["Продукты"]
name = "".join(name) # Продукты
print(name)
s_products = ", ".join(products) # молоко, масло, сметана, сливки, кефир, сыр
print(s_products)