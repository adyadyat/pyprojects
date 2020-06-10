annual_file = open("q1.txt")
annual_file1 = open("q2.txt")
annual_file2 = open("q3.txt")
annual_file3 = open("q4.txt")
annual = annual_file.read().strip()
annual1 = annual_file1.read().strip()
annual2 = annual_file2.read().strip()
annual3 = annual_file3.read().strip()
year_num = int(annual) + int(annual1) + int(annual2) + int(annual3)
annual_file.close()
annual_file1.close()
annual_file2.close()
annual_file3.close()

new_annual_report = open("year.txt", "w")
new_annual_report.write(str(year_num))
new_annual_report.close()

"""
# Читаем данные из qN файлов.
q1_file = open("q1.txt")
q1 = q1_file.read().strip()

q2_file = open("q2.txt")
q2 = q2_file.read().strip()

q3_file = open("q3.txt")
q3 = q3_file.read().strip()

q4_file = open("q4.txt")
q4 = q4_file.read().strip()

# Преобразовываем к числу и складывам.
year = int(q1) + int(q2) + int(q3) + int(q4)

# Обратно преобразовываем к строке.
year = str(year)

# Сохраняем в годовой отчет.
year_file = open("year.txt", "w")
year_file.write(year)
year_file.close()

ГОДОВОЙ ОТЧЕТ
Рядом с программой находятся 4 файла: q1.txt, q2.txt, q3.txt и q4.txt.
Каждый файл содержит целое число — квартальную прибыль компании.

Напишите программу, 
которая читает все квартальные отчеты, 
суммирует результат и сохраняет его в файл year.txt.

После того как программа выполнится, 
система сама откроет файл year.txt и проверит его содержимое.
"""