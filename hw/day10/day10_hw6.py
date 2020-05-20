print("Enter size: ",end="")
n = int(input())
print("Enter type 0 or 1: ",end="")
st = "*"
sp = " "
t = int(input())
for i in range(1,n+1):
	if i==1:
		print(sp,end="")
		for x in range(1,n+1):
			print(x,end="")
		print()
	for j in range(1,n+1):
		if j==1:
			print(i,end="")
		if i%2!=0:
			if j%2!=t:
				print(st,end="")
			else:
				print(sp,end="")
		if i%2==0:
			if j%2==t:
				print(st,end="")
			else:
				print(sp,end="")
	print()