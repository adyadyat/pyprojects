for i in range(8,0,-1):
	for x in range(8,i,-1):
		print(" ",end="")
	for j in range(i,0,-1):
		print(j,end="")
		print(" ",end="")
	print()
for i in range(8,0,-1):
	for x in range(0,i-1):
		print(" ",end="")
	for j in range(8,i-1,-1):
		print(j,end="")
		print(" ",end="")
	print()
"""
8 7 6 5 4 3 2 1 
 7 6 5 4 3 2 1 
  6 5 4 3 2 1 
   5 4 3 2 1 
    4 3 2 1 
     3 2 1 
      2 1 
       1 
       8 
      8 7 
     8 7 6 
    8 7 6 5 
   8 7 6 5 4 
  8 7 6 5 4 3 
 8 7 6 5 4 3 2 
8 7 6 5 4 3 2 1 
"""