n = int(input())
a = 1
i = 1
c = 1
while i <= n+1:
	for j in range(a, i + 1):
		print(a, end="")
		c +=1
		print()
	a += 1
	i = c + 1