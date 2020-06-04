import sys
first_name = sys.argv[1]
last_name = sys.argv[2]
middle_name = sys.argv[3]
first_name = first_name.capitalize()
last_name = last_name.capitalize()
middle_name = middle_name.capitalize()
print(last_name, first_name, middle_name)

# метод строки .capitalize() = первый символ строки верхний регистр