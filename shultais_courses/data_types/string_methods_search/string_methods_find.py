languages = "Языки: Python, PHP, SQL, HTML, Java."
langs_positions = languages.find(": ")
print(langs_positions) # 5 - индекс :

languages = languages[langs_positions + 2:]
print(languages) # Python, PHP, SQL, HTML, Java.

second_language_start_positions = languages.find(", ") + 2 # 8 индекс
second_language_end_positions = languages.\
	find(", ", second_language_start_positions) # 11 индекс
second_language = languages[second_language_start_positions:second_language_end_positions] # [8:11]
print(second_language) # [8:11] PHP

last_language_positions = languages.rfind(", ") + 2 # 24 индекс "J"
last_language = languages[last_language_positions:].strip(".") # [24:без "."]
print(last_language) # Java

# S.find(str, [start],[end]) Поиск подстроки в строке. 
# Возвращает номер первого вхождения или -1
# S.rfind(str, [start],[end]) Поиск подстроки в строке. 
# Возвращает номер последнего вхождения или -1