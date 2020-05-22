def num_sum(a):
	res=0
	for i in range(1,a+1):
		res+=i
		print(i,end="")
		print(" ",end="")
	print("=",end="")
	print(res,end="")
	print()
def num_sum_kv(a):
	res=0
	for i in range(1,a+1):
		res+=i**2
		#print(i,end="")
		#print(" ",end="")
	print("= ",end="")
	print(res,end="")
	print()
num_sum_kv(10)
num_sum_kv(20)
