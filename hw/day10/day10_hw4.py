c = 1
x = 0
n = int(input())
for i in range(1,n+1):
	for j in range(1,n+1):
		if c<10 or x==9:
			print(" ",end="")
		if i%2!=0:
			print(c,end="")
			c+=1
		if i%2==0:
			print(x,end="")
			x-=1
			c+=1
		print(" ",end="")
	x=c+(n-1)
	print()

'''
 1  2  3  4  5  6  7  8 
16 15 14 13 12 11 10 9 
17 18 19 20 21 22 23 24 
32 31 30 29 28 27 26 25 
33 34 35 36 37 38 39 40 
48 47 46 45 44 43 42 41 
49 50 51 52 53 54 55 56 
64 63 62 61 60 59 58 57 
'''