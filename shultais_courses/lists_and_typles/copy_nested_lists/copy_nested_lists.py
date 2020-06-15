from copy import deepcopy

cities = [
			["Moscow", 12_000_000], 
			["Saint-Petersburg", 5_300_000], 
			["Novosibirsk", 1_600_000],
			["Kaliningrad", 480_000], 
			["Vladivostok", 605_000],
			["Kyev", 2_900_000], 
			["Minsk", 2_000_000]
]

cities_copy = deepcopy(cities)
#cities_copy = cities.copy()
# cities_copy = cities[:] Альтернативный вариант копирования списка
cities[0][0] = "Москва"
cities[1] = ["Казань", 1_200_000]
cities_copy.append(["Красноярск", 1_000_000])

print(cities)
print(cities_copy)
print(cities[0] is cities_copy[0])