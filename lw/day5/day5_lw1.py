tr = 0
pr = ""
br = 3
pr1 = "   "
a = 1
for i in range(1,10):
	print(pr, end="")
	print(i, end="")
	print(pr1, end="")
	print(a, end="")
	print()
	a += 1
	pr += " "
	tr += 1
	if tr % br == 0:
		pr = ''
		a = 1
	print()
	
'''
1   1

 2   2

  3   3

4   1

 5   2

  6   3

7   1

 8   2

  9   3

'''