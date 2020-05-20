for i in range(1,9):
	for j in range(1,i+1):
		print(i,end='')
		print(' ',end="")
	for k in range(8,i,-1):
		print(' '*4,end='')
	for x in range(1,i+1):
		print(i,end='')
		print(' ',end="")
	print()

for i in range(8,0,-1):
	for j in range(1,i+1):
		print(i,end="")
		print(' ',end="")
	for k in range(8,i,-1):
		print(' '*4,end='')
	for x in range(1,i+1):
		print(i,end='')
		print(' ',end="")
	print()

'''
1              1
22            22
333          333
4444        4444
55555      55555
666666    666666
7777777  7777777
8888888888888888
8888888888888888
7777777  7777777
666666    666666
55555      55555
4444        4444
333          333
22            22
1              1
'''