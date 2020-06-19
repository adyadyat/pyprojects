user = {
	"age": 18,
	"first_name": "Askar",
	"is_active": True,
	"roles": [17, 48],
	"address": {"city": "Москва", "street": "Гагарина", "house": 22}
}

profile = {
	"age": 22,
	"first_name": "Nikita",
	"last_name": "Ivanov",
	"email": "user@domain.com"
}

del user["age"]
user["last_name"] = "Иванов"
#user["age"] += 1
user["is_active"] = False
user.update(profile)
user.update(first_name="Nik", age=15)

print(user)