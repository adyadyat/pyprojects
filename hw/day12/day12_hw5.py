x = 0
c = 4
n = int(input())
for i in range(1,n):
	print(i,end="")
	print(" ",end="")
	x = i
	for j in range(1,i):
		x += c
		c -= 1
		print(x,end="")
		print(" ",end="")
	c = n-2
	print()
"""
n = int(input(6))
1 
2 6 
3 7 10 
4 8 11 13 
5 9 12 14 15 
"""