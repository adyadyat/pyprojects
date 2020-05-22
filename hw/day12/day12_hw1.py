n = int(input())
for i in range(1,n):
	for x in range(0,i-1):
		print(" ",end="")
	for j in range(i,n):
		print(j,end="")
		print(" ",end="")
	print()
for i in range(n-2,0,-1):
	for x in range(0,i-1):
		print(" ",end="")
	for j in range(i,n):
		print(j,end="")
		print(" ",end="")
	print()
"""
1 2 3 4 5 6 7 
 2 3 4 5 6 7 
  3 4 5 6 7 
   4 5 6 7 
    5 6 7 
     6 7 
      7 
     6 7 
    5 6 7 
   4 5 6 7 
  3 4 5 6 7 
 2 3 4 5 6 7 
1 2 3 4 5 6 7 
"""