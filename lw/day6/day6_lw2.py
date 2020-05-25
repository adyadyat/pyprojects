print("Enter your number: ", end="")
n = int(input())
d = 2
stop = True
while stop:
	if n % d == 0:
		n /= d
		print(d, end="")
		print(" - ", end="")
		print(n)
	else:
		d += 1
	if n == d:
		print(d, end="")
		stop = False