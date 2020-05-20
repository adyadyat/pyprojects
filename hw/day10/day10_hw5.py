c = 1
x = 0
n = int(input())
for i in range(1,n):
	if i%2==0:
		for j in range(n-1,0,-1):
			if x == 9:
				print(" ",end="")
			print(x,end="")
			print(" ",end="")
			x-=1
			c+=1
	if i%2!=0:
		for j in range(1,n):
			if c<10:
				print(" ",end="")
			print(c,end="")
			print(" ",end="")
			c+=1
		x=c+(n-2)
	print()