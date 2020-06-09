import sys
name = sys.argv[1]

temp_file = open("template.txt", encoding="utf8")
temp = temp_file.read()

print(temp.replace("{{ name }}", name))