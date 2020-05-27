def factorial(f):
	sum=1
	for i in range(1,f+1):
		sum*=i
	return sum
f=int(input())
print(factorial(f))
	