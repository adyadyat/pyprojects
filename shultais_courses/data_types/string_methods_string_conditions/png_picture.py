import sys

png = sys.argv[1]
png = png.lower().endswith(".png")
print(png)

"""
PNG ИЗОБРАЖЕНИЕ?
Напишите программу, которая первым аргументом командной строки
принимает название файла, а после выводит True если это png изображение, 
и False в противном случае.
Определять png это или нет нужно по расширению файла.
Учитывайте, что имя может быть набрано в разных регистрах.
> python program.py photo.png
> True
> python program.py photo.jpg
> False
> python program.py ROOM.PNG
> True
"""