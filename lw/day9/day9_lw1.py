sum = 0
for i in range(1,9):
	print(i,end="")
	print(" ",end="")
	for j in range(1,i+1):
		print(j,end="")
		print(" ",end="")
		sum+=j
	print(" - ",end="")
	print(sum,end="")
	sum=0
	print()