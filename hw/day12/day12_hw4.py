n = int(input())
for i in range(1,n):
	for j in range(1,i+1):
		if j%2!=0:
			print(1,end="")
			print(" ",end="")
		else:
			print(0,end="")
			print(" ",end="")
	print()
"""
1 
1 0 
1 0 1 
1 0 1 0 
1 0 1 0 1 
1 0 1 0 1 0 
1 0 1 0 1 0 1 
"""