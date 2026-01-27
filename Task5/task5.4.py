cities = []

for i in range(5):
    city = input("Enter a city: ")

    if city not in cities:
        cities.append(city)

print(f"The Collected Cities are: {cities}")

if len(cities) < 5:
    print("If there are lesser number of cities than you entered, There must have been some repetition in the Input values!")
else:
    print("GoodBye!")