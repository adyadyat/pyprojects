import sys
heading = sys.argv[1] # '<p>текст</p><h1>Заголовок</h1><p>еще текст</p>'
h1_start = heading.find("1>") + 2 # 16 index Заголовок</h1><p>еще текст</p>'
h1_end = heading.find("</h") #  </h1><p>еще текст</p>'
head = heading[h1_start:h1_end] # вывод среза Заголовок
print(head) # Заголовок

# вывод заголовка h1