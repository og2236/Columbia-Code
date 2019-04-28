# ------------------------------------------------------------------------------
# GUESSING GAME
#
# by | Oskar Garcia OG2236 |
# Columbia University | ENGIE1006 | Spring 2019
# Project1 – Part 1 V.1.0
# V.1.0
# ______________________________________________________________________________

import random

# -- Program greeting

print("\nWelcome to the number guessing game!\n" +
      "You have five chances to make a guess.\n" +
      "Please follow the instructions carefully.\n")

#
# -- Generates initial game variables

goal = random.randint(1, 10)  # -- Generates and stores the game's goal
attempts = 0  # -- Tracks attempts and works as a switch to terminate the game
max_attempts = 5  # -- Sets the max number of attempts allowed before game ends
win = None  # -- Tracks game status

#
# -- Prompts the user for values, carries out computations and game dynamics

while attempts < max_attempts:
    user_input = int(input("\nPick any integer from 1 to 10: "))
    miss_range = abs(goal - user_input)  # -- Absolute difference goal-guess

    # -- Controls loop until correct guess or max attempts
    if miss_range == 0:
        print("\nCORRECT!")
        attempts = max_attempts
        win = True

    elif miss_range > 5:
        print("\nNot even close!")

    elif 3 <= miss_range <= 5:
        print("\nYou're close!")

    elif miss_range < 3:
        print("\nAlmost there!")

    attempts += 1  # -- Increments attempts if user missed the goal

#
# -- Displays the game's result

if win:
    print("\nYou win the game!")
else:
    print("but, YOU LOSE!", "\nThe correct number was", goal,
          "\nBetter luck next time!")
