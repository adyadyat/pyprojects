import sys
# 'Leading growth: why strategy matters'
text = sys.argv[1]

# Очищаем строку от пробелов strip(), применяем title() и добавляем точку.
text = text.strip().title() + "."

# Выводим текст.
print(text)