s = 0
for i in range(1,9):
	for j in range(1,i):
		print(0,end="")
	print(i,end="")
	for x in range(8,i,-1):
		print(0,end="")
	s+=1
	print()
"""
00000000
01000000
00200000
00030000
00004000
00000500
00000060
00000007
"""