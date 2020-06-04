import sys
pronoun = sys.argv[1]
pronoun = pronoun.\
	replace("I am", "I'm").\
	replace("You are", "You're").\
	replace("He is", "He's").\
	replace("She is", "She's").\
	replace("It is", "It's").\
	replace("We are", "We're").\
	replace("They are", "They're")
print(pronoun)

# S.replace(шаблон, замена, количество замен) Замена шаблона