for i in range(1,9):
	for j in range(8,i,-1):
		print(' ',end='')
	for k in range(1,i+1):
		print(i,end='')
	for x in range(2,i+1):
		print(i,end='')
	print()
for i in range(7,0,-1):
	for j in range(i,8):
		print(' ',end='')
	for k in range(i,0,-1):
		print(i,end='')
	for x in range(i,1,-1):
		print(i,end='')
	print()

'''
       1
      222
     33333
    4444444
   555555555
  66666666666
 7777777777777
888888888888888
 7777777777777
  66666666666
   555555555
    4444444
     33333
      222
       1
'''
