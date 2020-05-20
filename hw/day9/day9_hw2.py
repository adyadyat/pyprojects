for i in range(1,9):
	for j in range(8,i,-1):
		print(' ',end='')
	for k in range(1,i+1):
		print(i,end="")
	for x in range(1,i+1):
		print(i,end="")
	print()
for i in range(8,0,-1):
	for k in range(i,8):
		print(' ',end="")
	for j in range(i,0,-1):
		print(i,end='')
	for x in range(i,0,-1):
		print(i,end="")
	print()

'''
       11
      2222
     333333
    44444444
   5555555555
  666666666666
 77777777777777
8888888888888888
8888888888888888
 77777777777777
  666666666666
   55555555
    44444444
     333333
      2222
       11
'''