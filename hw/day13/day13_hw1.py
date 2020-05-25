def quad(a):
	res=0
	for i in range(1,a+1):
		res=i**i
		print(res,end="")
		print(" ",end="")
	print()
a=int(input())
quad(5)

def factorial(a):
	res=1
	for i in range(1,a+1):
		res*=i
		print(res,end="")
		print(" ",end="")
	print()
a=int(input())
factorial(a)