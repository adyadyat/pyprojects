user = {
	"age": 18,
	"first_name": "Askar",
	"is_active": True,
}
user.update(AGE=None)
#print(user["AGE"])
#print("AGE" in user)
#print("age" in user)
#print(user.get("AGE"))
print(user.get("AGE", 0) or 0)
print(user.get("age"))