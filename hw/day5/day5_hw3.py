tr = 0
pr = ""
pr1 = "++"
br = 3
sw = 0
for i in range(1,10):
	print(pr, end="")
	print(i, end="")
	print()
	tr += 1
	if sw == 0:
		pr += '-'
	elif sw == 1:
		pr += '+'
	if pr == '--':
		sw = 1
	if pr == '++':
		sw = 0
	if tr % br == 0:
		pr = ''
	print()
	
'''
1

-2

--3

4

-5

--6

7

+8

++9
'''