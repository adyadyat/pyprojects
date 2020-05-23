def quad(a):
	res=0
	for i in range(1,a+1):
		res=i**i
		print(res,end="")
		print(" ",end="")
	print()
quad(10)

def factorial(a):
	res=1
	for i in range(1,a+1):
		res*=i
		print(res,end="")
		print(" ",end="")
	print()
factorial(10)