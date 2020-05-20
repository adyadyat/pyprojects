print("Enter your number: ", end="")
n = int(input())
stop = 1
d = 1
c = 0
sum = 0
sum1 = 0
for i in range(2,n+1):
	if i == 2:
		print(i, end="")
		print(" is prime")
		sum += i
		stop = 0
	
	while stop == 1:
		if d == i and c < 2:
			print(i, end="")
			print(" is prime", end="")
			print()
			sum += i
			c = 0
			d = 1
			stop = 0
		if c > 1:
			print(i, end="")
			print(" is composite", end="")
			print()
			sum1 += i
			c = 0
			d = 1
			stop = 0
	
		if stop == 1:
			if i % d == 0:
				c += 1
	
		if stop == 1:
		    d += 1
	
		if i < d:
		    c = 0
		    d = 1
		    stop = 0

	if stop == 0:
		stop = 1
print("Result prime: ", sum)
print("Result composite: ", sum1)
'''
Вывод всех простых чисел до N
Сумма простых чисел
'''