# ------------------------------------------------------------------------------
# PERFECT NUMBERS
#
# by | Oskar Garcia OG2236, in collaboration with Marni Rosenthal MAR2341 |
# Columbia University | ENGIE1006 | Spring 2019
# In-class problem set 1 – Problem 4 V.1.0
# V.1.0
# ______________________________________________________________________________

#
# -- Program greeting

print("\nHello! This program helps you find out\n"
      + "if a positive integer is a Perfect Number\n")

#
# -- Prompts the user for a number and stores it in a variable

the_number = int(input("Please provide an integer greater than 1: "))

#
# -- Finds the factors for the given number by searching through candidates
#    with a while loop and checking divisibility by modulo operation

candidate = 1  # -- Variable for possible factors
factor_sum = 0  # -- Accumulator for the sum of found factors

if the_number % 2 != 0:  # -- Optimize by ruling out odd integers
    print("Your number is NOT a perfect number")

else:
    while candidate < the_number:
        if the_number % candidate == 0:
            factor_sum += candidate
        candidate += 1
    if factor_sum != the_number:
        print("Your number is NOT a perfect number")
    else:
        print("Your number IS a perfect number")
