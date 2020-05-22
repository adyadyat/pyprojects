n = int(input())
for i in range(1,n):
	for j in range(1,n):
		if i>1:
			if i == j:
				print(j,end="")
				print(" ",end="")
			else:
				print(0,end="")
				print(" ",end="")
		else:
			print(0,end="")
			print(" ",end="")
	print()
"""
00000000
02000000
00300000
00040000
00005000
00000600
00000070
00000008
"""