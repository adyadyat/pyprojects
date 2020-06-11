cities = ["Moscow", "Astana", "Almaty",
			 "Shu", "Almaty", "Kokshetau", "Kostanay"]
populations = [12000000, 5300000, 480000, 650000, 480000, 145000, 2000000]

cnt = cities.count("Almaty")
print(cnt)
print("Almaty" in cities)

Kokshetau_i = cities.index("Almaty", 3)

city = cities.pop(Kokshetau_i).upper()
print(city)

population = populations.pop(Kokshetau_i) / 1e6 # 1_000_000
print(population)

print(cities)
print(populations)