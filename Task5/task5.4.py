cities = []

for i in range(5):
    city = input("Enter a city: ")

    if city not in cities:
        cities.append(city)

print(f"The Collected Cities are: {cities}")