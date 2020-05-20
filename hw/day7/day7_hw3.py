n = 0
count = 0
sw = 0
for i in range(8,1-1,-1):
	print(i, end="")
	for j in range(7,1-1,-1):
		print(" ", end="")
		if n == 0:
			sw = 0
		if sw == 0:
			print(j, end="")
		if sw == 1:
			print(i, end="")
			n -= 1
	sw = 1
	count += 1
	n = count
	print()

'''

 8 7 6 5 4 3 2 1
 7 7 6 5 4 3 2 1
 6 6 6 5 4 3 2 1
 5 5 5 5 4 3 2 1
 4 4 4 4 4 3 2 1
 3 3 3 3 3 3 2 1
 2 2 2 2 2 2 2 1
 1 1 1 1 1 1 1 1

 '''