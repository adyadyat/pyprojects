first_name = "Askar"
first_name_l = ["Mihail"]

names = ["Ivan", "Alena", first_name, first_name_l, "Sergey", "Lisa"]


names[2] = "Oleg"
names[3][0] = "Oleg"
first_name_l[0] = "Svetlana"

print(names) # ['Ivan', 'Alena', 'Oleg', ['Oleg'], 'Sergey', 'Lisa']
print(first_name) # Askar
print(first_name_l) # ['Oleg'] ['Svetlana']