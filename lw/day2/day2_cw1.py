a = ''
b = '+'
n = int(input('Enter number: '))
for i in range(1, n +1):
	if (i % 2 == 0):
		print(b, end='')
		print(i, end='')
		b += '+'
	if (i % 2 != 0):
		print(a, end='')
		print(i, end='')
		a += '-'

	print()