contacts = {
	"email": "user@domain.com",
	"facebook": "username",
	"instagram": "@account",
}
contacts.update({
	"phone1": "+7 891 555-55-55",
	"phone2": "+7 891 222-22-22",
})

print(contacts)
print(contacts.pop("facebook")) # возвращает значение и удаляет из словаря
print(contacts.popitem()) # возвращает значение в виде кортежа послед
print(contacts.popitem())
print(contacts)