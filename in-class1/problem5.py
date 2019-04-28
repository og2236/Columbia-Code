# ------------------------------------------------------------------------------
# GREATEST COMMON DIVISOR
#
# by | Oskar Garcia OG2236, in collaboration with Marni Rosenthal MAR2341 |
# Columbia University | ENGIE1006 | Spring 2019
# In-class problem set 1 – Problem 5 V.1.0
# V.1.0
# ______________________________________________________________________________

#
# -- Program greeting

print("\nHello! This program helps you find the Greatest\n"
      + "Common Divisor for two different integers\n")

#
# -- Prompts the user for a pair of integer values such that a > b"

int_a = int(input("Please enter the biggest of the two integers: "))
int_b = int(input("Please enter the smaller of the two integers: "))

#
# -- Computes the GCD based on the given formula

while int_b != 0:
    remainder = int_a % int_b
    int_a = int_b
    int_b = remainder

#
# -- Displays the result for the user
print("The GCD between your two numbers is", int_a)

