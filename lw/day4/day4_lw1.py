p = 600
m = 0
s = 500
print("Выберите количество насосов:", end=' ')
n = int(input())
while p >= 200:
	if n == 1:
		print(p, end=' ')
		print(m)
		p -= 3
		m += 1
	if n == 2:
		print(p, end=' ')
		print(m)
		p -= 8
		m += 1
	