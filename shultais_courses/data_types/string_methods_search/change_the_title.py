import sys
title = sys.argv[1]
word = sys.argv[2]
title_start = title.find("<h1>") # 16 index
title_end = title.find("</h1>") # 25 index
title_lng = title[:title_start + 4]
title_lng_end = title[title_end:]
title_replace = title[title_start + 4:title_end] # заменяемое слово
title1 = word
print(title_lng)
print(title1)
print(title_lng_end)
print(title_lng + title1 + title_lng_end)
# <h1>......</h1> replace на аргумент[2]
# '<p>текст</p><h1>Заголовок</h1><p>еще текст</p>' 'Главный'
# '<p>Текст</p> <h1>Статья о пингвинах</h1> <p>Текст.</p>' Статья
# '<section><h1>Курс по JavaScript</h1></section>' "Введение в Python"
# '<h1>Заголовок</h1> <h2>Заголовок</h2>' "Основной заголовок"