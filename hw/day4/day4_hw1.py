import time
p = 600
m = 0
s = 0
sw = 0
print("Выберите количество насосов:", end=' ')
n = int(input())
while p >= 200:
	print(p, end='-')
	print(m, end=' ')

	if sw == 0:
		if n == 1:
			p -= 3
			m += 1
		if n == 2:
			p -= 5
			m += 1
		if n == 3:
			p -= 8
			m += 1

	if p <= 250:
		sw = 1

	if sw == 1:
		p += 9
		m += 1
		s = p
	if s > 500:
		sw = 3
		
	print()
	time.sleep(0.2)
'''
1 - первый насос
2 - второй насос
3 - оба насоса
'''