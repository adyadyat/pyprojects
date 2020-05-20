

for i in range(1, 11):
	if i % 2 == 0:
		print("+", end='')
		print(i, end='')
	if i % 2 == 1:
		print(i, end='')
		print("-", end='')
	print()