tr = 0
pr = ""
pr1 = "++"
br = 3
sw = 0
for i in range(1,10):
	print(pr, end="")
	print(i, end="")
	print()
	pr += "-"
	tr += 1
	if pr == '--':
		pr = pr1
	if tr % br == 0:
		pr = ''
	print()
	
'''
1

-2

++3

4

-5

++6

7

-8

++9
'''