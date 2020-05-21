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