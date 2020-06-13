cities = ["Moscow", "Saint-Petersburg", "Novosibirsk",
			 "kaliningrad", "Vladivostok", "Kyev", "Minsk"]
populations = [12000000, 5300000, 1600000, 480000, 605000, 2900000, 2000000]

# cities.sort(key=str.upper)
# cities.sort(key=len)
#cities.sort(key=len, reverse=True) # метод sort() не возвращает значение
#cities = cities.sort(key=len, reverse=True) # None
sorted_cities = sorted(cities, key=len, reverse=True) # Метод sorted() возвращает значение
# populations.sort()
populations.sort(reverse=True)

print(cities) # Исходный список
print(sorted_cities) # Отсортированный
print(populations)