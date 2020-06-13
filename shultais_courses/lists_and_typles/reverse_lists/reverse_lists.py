cities = ["Moscow", "Saint-Petersburg", "Novosibirsk",
			 "Kaliningrad", "Vladivistok", "Kyiv", "Minsk"]
populations = [12_000_000, 5_300_000, 1_600_000,
				 480_000, 605_000, 290_000, 200_000]

cities.reverse() # Не возвращает значения
populations = list(reversed(populations))
populations = populations[::-1]

print(cities)
print(populations)