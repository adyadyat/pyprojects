listA = [1,2,3,4,5,6,7,8,9]
listE = []
listO = []
for i in listA:
	if i % 2 != 0:
		listO.append(i)
		if i < 9:
			listO.append(0)
	if i % 2 == 0:
		listE.append(0)
		listE.append(i)
		if i == 8:
			listE.append(0)
print(listO)
print(listE)

"""
[1, 0, 3, 0, 5, 0, 7, 0, 9]
[0, 2, 0, 4, 0, 6, 0, 8, 0]
"""