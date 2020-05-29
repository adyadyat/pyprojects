myListEven = []
myListOdd = []
for i in range(10):
	a = int(input("Enter number: "))
	if a % 2 == 0:
		myListEven.append(a)
	if a % 2 != 0:
		myListOdd.append(a)
print(myListEven)
print(myListOdd)
sE = 0
sO = 0
for i in range(len(myListEven)):
	sE += myListEven[i]
for i in range(len(myListOdd)):
	sO += myListOdd[i]
print(sE)
print(sO)