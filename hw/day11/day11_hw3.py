countJ = 0
step = 0
sw = 1
countI = 0
symbol = ""
#n = int(input())
for i in range(1,9):
	if countI==32:
		countI=0
	if countI<16:
		step=1
	else:
		step=2
	for j in range(1,9):
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
* *     * *     
* *     * *     
    * *     * * 
    * *     * * 
* *     * *     
* *     * *     
    * *     * * 
    * *     * * 
"""