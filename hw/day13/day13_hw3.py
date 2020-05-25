def division():
	n=int(input())
	d=2
	count=0
	stop=True
	while stop:
		if n%d==0:
			n/=d
			count+=1
			print(d,end="")
			print(" ", end="")
		if n==1:
			if count==1:
				print("is prime number",end="")
			stop=False
		if n%d!=0:
			d+=1
	print()
division()

"""
Наименьшие делители числа
Нахождение простого числа
"""