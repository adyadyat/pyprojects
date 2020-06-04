import sys
num = sys.argv[1]
num = num.\
	replace("0", "a").\
	replace("1", " ").\
	replace("2", "b").\
	replace("3", "e").\
	replace("4", "l").\
	replace("5", "mu").\
	replace("6", "n").\
	replace("7", "o").\
	replace("8", "lee").\
	replace("9", "f")
print(num)

# замена цифр 89514568156. на буквы методом replace()