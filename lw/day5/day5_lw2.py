tr = 0
pr = ""
br = 1
pr1 = "   "
a = 0
for i in range(1,31):
	print(pr, end="")
	print(i, end="")
	print()
	pr += " "
	tr += 1
	if tr % br == 0:
		pr = ''
		tr = 0
		br += 1
	print()

'''
1

2

 3

4

 5

  6

7

 8

  9

   10

11

 12

  13

   14

    15

16

 17

  18

   19

    20

     21

'''