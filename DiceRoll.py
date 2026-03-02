#DiceRoll.py
#Name:Erick Andres
#Date:3/1/2026
#Assignment: Lab 6
# purpose: program to simulate rolling two dices multiple times.
#  
import random

def main():
    rolls = int(input("How many times should the dice be rolled"))

    if rolls <= 0:
        print("Number of rolls must be positive.")
        return 

    #Create an empty list with possible roll values
    counts = {}

    #Create two dice values ranging from 1 - 6 each
    for total in range (2, 13):
        counts[total] = 0 

    #find the sum total of the two dice
    for i in range(rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        counts[total] += 1

    #print statictics for dice rolls
    print("\nResults:")
    for total in range(2, 13):
        count = counts[total]
        percentage = (count / rolls) * 100
        print(total, ":", count, "(", f"{percentage:.2f}%", ")")


if __name__ == '__main__':
    main()
 