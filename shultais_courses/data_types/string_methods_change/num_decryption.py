import sys
num = sys.argv[1]
num = num.\
	replace("a", "0").\
	replace(" ", "1").\
	replace("b", "2").\
	replace("lee", "8").\
	replace("e", "3").\
	replace("l", "4").\
	replace("mu", "5").\
	replace("n", "6").\
	replace("o", "7").\
	replace("f", "9")
print(num)

# замена цифр 89514568156. на буквы методом replace()