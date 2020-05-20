for i in range(1,9):
	for j in range(8,i-1,-1):
		print(j, end="")
		print(" ", end="")
	print()
print("---------------------")
for i in range(8,0,-1):
	for j in range(i,0,-1):
		print(i, end="")
		print(" ", end="")
	print()
print("---------------------")
for i in range(8,0,-1):
	for j in range(i,0,-1):
		print(j, end="")
		print(" ", end="")
	print()
print("---------------------")
for i in range(1,9):
	for j in range(i,9):
		print(j, end="")
		print(" ", end="")
	print()
print("---------------------")
for i in range(1,9):
	for j in range(i,9):
		print(i, end="")
		print(" ", end="")
	print()
print("---------------------")
for i in range(8,0,-1):
	for j in range(1,i+1):
		print(j, end="")
		print(" ", end="")
	print()

"""
8 7 6 5 4 3 2 1 
8 7 6 5 4 3 2 
8 7 6 5 4 3 
8 7 6 5 4 
8 7 6 5 
8 7 6 
8 7 
8 
---------------------
8 8 8 8 8 8 8 8 
7 7 7 7 7 7 7 
6 6 6 6 6 6 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
---------------------
8 7 6 5 4 3 2 1 
7 6 5 4 3 2 1 
6 5 4 3 2 1 
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
---------------------
1 2 3 4 5 6 7 8 
2 3 4 5 6 7 8 
3 4 5 6 7 8 
4 5 6 7 8 
5 6 7 8 
6 7 8 
7 8 
8 
---------------------
1 1 1 1 1 1 1 1 
2 2 2 2 2 2 2 
3 3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 
6 6 6 
7 7 
8 
---------------------
1 2 3 4 5 6 7 8 
1 2 3 4 5 6 7 
1 2 3 4 5 6 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""