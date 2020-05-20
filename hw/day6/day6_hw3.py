print("Enter your number: ", end="")
n = int(input())
stop = 1
d = 1
c = 0
sum = 0
sum1 = 0
prime = []
composite = []
i = 2
while stop == 1:
	if d == i and c < 2 or i == 2:
		prime.append(i)
		sum += i
		c = 0
		d = 1
		i += 1
		stop = 0
			
	if c > 1:
		composite.append(i)
		sum1 += i
		c = 0
		d = 1
		i += 1
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
	if i > n:
		stop = 0

print(prime, end=" ")
print("is prime", end=" ")
print("Result: ", sum)
print(composite, end=" ")
print("is composite", end=" ")
print("Result: ", sum1)