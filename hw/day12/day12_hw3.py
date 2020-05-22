n = int(input())
for i in range(1,n):
	for j in range(1,i+1):
		print(j,end="")
		print(" ",end="")
	for x in range(i-1,0,-1):
		print(x,end="")
		print(" ",end="")
	print()
"""
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 
1 2 3 4 5 6 5 4 3 2 1 
1 2 3 4 5 6 7 6 5 4 3 2 1 
"""