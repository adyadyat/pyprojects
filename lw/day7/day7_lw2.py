sum = 0
total = 0
for i in range(1,9):
	for j in range(1,9):
		print(i, end="")
		sum += i
		total += i
	print("-", end="")
	print(sum, end="")
	sum = 0
	print()
print(total)

sum1 = 0
total1 = 0
for k in range(1,9):
	for m in range(1,9):
		print(m, end="")
		sum1 += m
	print("-", end="")
	print(sum1, end="")
	total1 += sum1
	sum1 = 0
	print()
print(total1)