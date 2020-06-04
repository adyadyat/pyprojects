import sys
word = sys.argv[1] # '<b>с</b><b>л</b><b>о</b><b>в</b><b>о</b>'
word = word.replace("</b><b>", "")
print(word) # <b>слово</b> Удаление внутренних тегов