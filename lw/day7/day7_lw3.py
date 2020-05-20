n = 0
sum = 0
for i in range(1,9):
	for j in range(1,9):
		n += 1
		sum += n
		if n < 10:
			print(" ", end="")
		if n % 7 == 0:
			if n < 10:
				print("X", end="")
			else:
				print("XX", end="")
		else:
			print(n, end="")
		print(" ", end="")
	#print(sum, end="")
	print()

"""
H0meWork:

"""