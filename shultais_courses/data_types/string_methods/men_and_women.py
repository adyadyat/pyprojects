import sys
word = sys.argv[1]
men = word.count("m")
women = word.count("w")
print("m (" + str(men) + ")", men * "*")
print("w (" + str(women) + ")", women * "*")

"""
Получаемый аргумент = wmwmwwmmwmw
вывод = m (8) ********
вывод = w (11) ***********
"""