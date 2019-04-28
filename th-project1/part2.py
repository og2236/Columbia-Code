# ------------------------------------------------------------------------------
# INVERSE GUESSING GAME
#
# by | Oskar Garcia OG2236 |
# Columbia University | ENGIE1006 | Spring 2019
# Project1 – Part 2 V.1.0
# V.1.0
# ______________________________________________________________________________

# -- Program greeting

print("\nWelcome to the inverse number guessing game!\n" +
      "The computer has 3 chances to guess your number.\n" +
      "Please follow the instructions carefully.\n")

#
# -- Defines game variables and controls game dynamics

attempts = 0  # -- Tracks attempts and serves as switch to terminate the game
max_attempts = 3  # -- Max attempts allowed by the computer
win = None  # -- Tracks game status

min_value = 1  # -- Lower bound in search range
max_value = 10  # -- Higher bound in search range

print("Please pick an integer between 1 and 10\nand hold it in your mind.")

while attempts < max_attempts:
    mid_value = (min_value + max_value) // 2  # -- Mid value from int division
    print("\nIs", mid_value, "your number?")
    user_input = int(input("\nType 1 = too big, 2 = too small, 3 = correct: "))

    if user_input == 3:
        print("\nI guessed right!")
        attempts = max_attempts
        win = True

    elif user_input == 2:
        min_value = mid_value + 1  # -- Sets lower bound to mid - 1

    elif user_input == 1:
        max_value = mid_value - 1  # -- Sets higher bound to mid + 1

    attempts += 1

if win:
    print("Computer Wins!")
else:
    print("\nAwww...Computer Loses")
