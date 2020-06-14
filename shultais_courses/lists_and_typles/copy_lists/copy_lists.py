cities = ["Moscow", "Saint-Petersburg", "Novosibirsk", 
			"Kaliningrad", "Vladivostok", "Kyev", "Minsk"]

cities_copy = cities.copy()
# cities_copy = cities[:] Альтернативный вариант копирования списка
print(cities_copy == cities, cities_copy is cities)


cities[0] = "Москва"
cities_copy[-1] = "Минск"

print(cities)
print(cities_copy)