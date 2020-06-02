listA = [1,2,3,4,5,6,7,8,9]
res = 0
for i in range(len(listA)-1):
	res = listA[i] + listA[i + 1]
	print(res, end=" ")
	res = 0
print()