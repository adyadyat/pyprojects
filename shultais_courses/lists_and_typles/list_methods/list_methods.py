cities = ["Moscow", "Astana", "Almaty"]
populations = [12000000, 5300000, 480000]

new_cities = ["Shu", "Almaty", "Kokshetau", "Kostanay"]
new_populations = [650000, 480000, 145000, 95000]

cities.append("Bishkek")
populations.append(1100000)

cities.insert(2, "Osh")
populations.insert(2, 1500000)

cities.extend(new_cities)
populations.extend(new_populations)

cities.extend(["Erevan"])

cities.remove("Almaty")
cities.remove("Almaty")

del cities[3]
# Для удаления по индексу, используется метод pop.
cities.pop(5)

populations.clear()

print(cities)
print(populations)