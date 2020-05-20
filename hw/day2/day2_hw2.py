cd d	a = ''
sw = 0
print('Enter yout number: ', end='')
number = int(input())
for i in range(1,number+1):
	print(a,end='')
	print(i,end='')
	if (sw == 0):
		a = '+' * i
		sw += 1
	else:
		if sw == 1:
			a = '=' * i
			sw += 1
		else:
			if sw == 2:
				a = '-' * i
				sw = 0
	print()

'''Task
1
+2
==3
---4
++++5
=====6
------7
'''