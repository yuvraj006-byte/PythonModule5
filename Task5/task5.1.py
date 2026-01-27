import random
num_dice = int(input("Enter the Numbers of dice to roll: "))

total = 0
print("The rolls are: ")
for i in range(num_dice):
    roll = random.randint(1, 6)
    total += roll


    print(roll, end = " ")
print()
print("The sum of all the rolls is: ", total)