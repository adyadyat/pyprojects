user = {
	"age": 18,
	"first_name": "Никита",
	"is_active": True,
	"role": "manager"
}

print(user.keys()) # dict_keys(['age', 'first_name', 'is_active', 'role'])
print(list(user.keys())[0]) # age
print(list(user)) # ['age', 'first_name', 'is_active', 'role']

print(user.values()) # dict_values([18, 'Никита', True, 'manager'])
print(list(user.values())) # [18, 'Никита', True, 'manager']

print(user.items()) # dict_items([('age', 18), ('first_name', 'Никита'), ('is_active', True), ('role', 'manager')])
print(list(user.items())) # [('age', 18), ('first_name', 'Никита'), ('is_active', True), ('role', 'manager')]

