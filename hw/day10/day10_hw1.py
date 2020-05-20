print("Enter type 0 or 1: ", end="")
n = int(input())
for i in range(1,9):
	for j in range(1,9):
		if i %2==n:
			if j%2==0:
				print("*", end="")
			else:
				print(" ", end="")
		if i%2!=n:
			if j%2!=0:
				print("*", end="")
			else:
				print(" ", end="")
	print()

"""
Выберите шахматную доску 0 или 1: 1
 * * * *
* * * * 
 * * * *
* * * * 
 * * * *
* * * * 
 * * * *
* * * * 
Выберите шахматную доску 0 или 1: 0
* * * * 
 * * * *
* * * * 
 * * * *
* * * * 
 * * * *
* * * * 
 * * * *
"""