for i in range(1,9):
	#print("*",end="")
	for j in range(1,9):
		if i == j or i == (8-j):
			print("*", end="")
		else:
			print(" ", end="")
	print()