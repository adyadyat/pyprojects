count = 0
step = 0
symbol = ""
n = int(input())
for i in range(1,n+1):
	if i%2!=0:
		step=1
	if i%2==0:
		step=2
	for j in range(1,n+1):
		count+=1
		if step==1:
			if count<=2:
				symbol="*"
			else:
				symbol=" "
		if step==2:
			if count<=2:
				symbol=" "
			else:
				symbol="*"
		print(symbol,end="")
		print(" ",end="")
		if count==4:
			count=0
	count=0
	print()
"""
8
* *     * *     
    * *     * * 
* *     * *     
    * *     * * 
* *     * *     
    * *     * * 
* *     * *     
    * *     * * 
"""