for i in range(1, 11):
	if i % 5 == 0:
		print(i, end='')
		print("#", end='')
	else:
		if i % 3 == 0:
			print(i, end='')
			print("*", end='')
		else:
			if i % 2 == 0:
				print(i, end='')
				print("+", end='')
			if i % 2 == 1:
				print(i, end='')
				print("-", end='')
	print()