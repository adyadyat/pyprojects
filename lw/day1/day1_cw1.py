

for i in range(1, 11):
	if i % 2 == 0:
		print(i, end='')
		print("+", end='')
	if i % 2 == 1:
		print(i, end='')
		print("-", end='')
	print()