
for i in range(1,9):
	for j in range(9,i+1,-1):
		print(" ",end="")
	for k in range(1,i+1):
		print(k,end="")
	print()

for i in range(8,0,-1):
	for j in range(9,i+1,-1):
		print(" ",end="")
	for k in range(1,i+1):
		print(k,end="")
	print()

'''
pr = "========"
for i in range(1,9):
	pr=pr[0:-1]
	print(pr,end="")
	for k in range(1,i+1):
		print(k,end="")
	print()
'''