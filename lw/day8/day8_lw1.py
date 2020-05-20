for i in range(1,9):
	for j in range(1,i+1):
		print(i, end="")
	print()
print("-----------------")
for k in range(1,9):
	for m in range(1,k+1):
		print(m, end="")
	print()
print("-----------------")
for x in range(1,9):
	for z in range(x,0,-1):
		print(z, end="")
	print()
print("-----------------")
for g in range(8,0,-1):
	for d in range(g,9):
		print(d, end="")
	print()
print("-----------------")
for g in range(8,0,-1):
	for d in range(g,9):
		print(g, end="")
	print()
print("-----------------")
for g in range(8,0,-1):
	for d in range(8,g-1,-1):
		print(d, end="")
	print()

'''
1
22
333
4444
55555
666666
7777777
88888888
-----------------
1
12
123
1234
12345
123456
1234567
12345678
-----------------
1
21
321
4321
54321
654321
7654321
87654321
-----------------
8
78
678
5678
45678
345678
2345678
12345678
-----------------
8
77
666
5555
44444
333333
2222222
11111111
-----------------
8
87
876
8765
87654
876543
8765432
87654321

'''