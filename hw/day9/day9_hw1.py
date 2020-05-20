for i in range(1,9):
	for j in range(8,i,-1):
		print(' ',end='')
	for k in range(1,i+1):
		print(i,end="")
	print()
for i in range(8,0,-1):
	for k in range(i,8):
		print(' ',end="")
	for j in range(i,0,-1):
		print(i,end='')
	print()


'''
       1
      22
     333
    4444
   55555
  666666
 7777777
88888888
88888888
 7777777
  666666
   55555
    4444
     333
      22
       1
'''