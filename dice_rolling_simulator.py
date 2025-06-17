import os
import random

# Tuple with ASCII art to represent the dices
DICE_ART = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│    ●    │",
        "│    ●    │",
        "│    ●    │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}


dice = [] # List of dices
total = 0 # Total sum of dices


while True:
    # Player input -> How many dices to play with
    number_of_dice = int(input("How many dice?: "))

    # Add random dices to list
    for i in range(number_of_dice):
        dice.append(random.randint(1, 6))

    # Output -> Print Dices
    for line in range(5):
        for die in dice:
            print(DICE_ART.get(die)[line], end="")
        print()

    # Total
    for die in dice:
        total += die

    # Print total
    print(f"Total: {total}")

    while True:
        rematch = input("\nWould you like to play again?(Y/n): ")
        if rematch in ["Y", "y"]:
            dice = []
            break
        elif rematch == "n":
            exit()
        else:
            print("Invalid input. Please try again\n\n")