n = 0
sw = 0
sum_of_hidden = 0
sum_of_reset = 0
d = int(input())
for i in range(1,9):
	n += 1
	for j in range(1,9):
		sw += 1
		print(" ", end="")
		if sw % d == 0:
			print(" ", end="")
			sum_of_hidden += n
		else:
			sum_of_reset += n
			print(n, end="")
	print()
print("sum of hidden numbers: ", end="")
print(sum_of_hidden)
print("sum of reset numbers: ", end="")
print(sum_of_reset)


'''

 1 1 1 1 1   1 1
 2 2 2   2 2 2 2
 3   3 3 3 3 3  
 4 4 4 4 4   4 4
 5 5 5   5 5 5 5
 6   6 6 6 6 6  
 7 7 7 7 7   7 7
 8 8 8   8 8 8 8
sum of hidden numbers: 45
sum of reset numbers: 243

'''