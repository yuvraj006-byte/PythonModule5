cities = []

for i in range(5):
    city = input("Enter a city: ")
    cities.append(city)


unique = set(cities)
print(f"The Collected Cities are: {unique}")