count_even=0
count_odd=0
temp_even=0
temp_odd=0
temp_odd1=0
print("enter number: ")
stop=True
while stop:
	n=int(input())
	print(n,end=" ")
	if n%2==0:
		if n>temp_even:
			temp_even=n
			count_even+=1
			print("count_even",count_even)
	if count_even==2:
		stop=False
"""
def even():
	n=int(input())
	print(n)
	temp=0
	count=0
	if n%2==0:
		count+=1
		temp=n
		if n>temp and count==2:
			print("stop")
	else:
		return even()
a=even()
print(a)
"""
'''
Вводить числа пока второе четное число будет больше предыдущего четного числа
Вводить числа пока второе нечетное число будет меньше предыдущего нечетного числа
'''