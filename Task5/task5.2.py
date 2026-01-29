nums = []

while True:
    user_input = input("Enter a number: ")

    if user_input == "":
        print("Goodbye")
        break

    nums.append(float(user_input))

nums.sort(reverse=True)

print("The five Greatest numbers are:")
for num in nums[:5]:
    print(num)


