for i in range(1,8):
	for j in range(1,8):
		if i==j or i==1 or i==7 or j==1 or j==7 or i==8-j:
			print("*",end="")
		else:
			print(" ",end="")
	print()
		