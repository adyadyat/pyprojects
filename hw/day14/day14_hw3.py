def even():
	n=int(input())
	count_even=0
	temp_even=0
	if count_even==2:
		return 1
	if n%2==0:
		if n>temp_even:
			temp_even=n
			count_even+=1
			return count_even+even()
print(even())





"""
count_odd=0
temp_odd=0
temp_odd1=0
print("enter number: ")
stop=True
while stop:
	
	print(n,end=" ")
	if n%2==0:
		if n>temp_even:
			temp_even=n
			count_even+=1
			print("count_even",count_even)
	if count_even==2:
		stop=False
"""