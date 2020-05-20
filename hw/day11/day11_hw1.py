countJ = 0
step = 0
countI = 0
symbol = ""
print("Enter type chess desk 1 or 2: ")
tp = int(input())
print("Enter range chess desk X=X: ")
n = int(input())
for i in range(1,n+1):
	if countI==n*4:
		countI=0
	if tp==1:
		if countI<n*2:
			step=1
		else:
			step=2
	else:
		if countI<n*2:
			step=2
		else:
			step=1
	for j in range(1,n+1):
		countI+=1
		countJ+=1
		if step==1:
			if countJ<=2:
				symbol="*"
			else:
				symbol=" "
		if step==2:
			if countJ<=2:
				symbol=" "
			else:
				symbol="*"
		print(symbol,end="")
		print(" ",end="")
		if countJ==4:
			countJ=0
	countJ=0
	print()
"""
Enter type chess desk 1 or 2: 
1
Enter range chess desk X=X: 
16
**  **  **  **  
**  **  **  **  
  **  **  **  **
  **  **  **  **
**  **  **  **  
**  **  **  **  
  **  **  **  **
  **  **  **  **
**  **  **  **  
**  **  **  **  
  **  **  **  **
  **  **  **  **
**  **  **  **  
**  **  **  **  
  **  **  **  **
  **  **  **  **
"""