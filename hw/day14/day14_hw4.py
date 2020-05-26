def prime(n,d):
	count=0
	if n==1 and count==1:
		print("is prime number",end="")
	if n%2==0:
		count+=1
	if n%d!=0:
		return prime(n,d+1)


n=int(input())
d=2
if n>1:
	print(prime(n,d))
else:
	print("Введите цифру больше двух")
'''
написать функцию, 
используя рекурсию, 
чтобы проверить, 
является ли число простым
'''