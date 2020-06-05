import sys
file_ext = sys.argv[1]
file_start = file_ext.rfind(".") +1
print(file_ext[file_start:].lower())
# вывод расширения в нижний регистр
# my_car.png
# photo1.JPEG
# task_928.v2.py 
"""
import sys

filename = sys.argv[1]

# Ищем первую точку справа с помощью rfind.
latest_dot_index = filename.rfind(".")

# Берем правильный индекс.
ext = filename[latest_dot_index+1:]

# Применяем lower перед выводом.
print(ext.lower())
"""