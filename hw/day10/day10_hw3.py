for i in range(1,):
	for j in range(1,10):
		if i==j or i==1 or i==9 or j==1 or j==9 or i==10-j or j==5 or i==5:
			print("*",end="")
			print(" ",end="")
		else:
			print("  ",end="")
	print()

