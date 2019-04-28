# ------------------------------------------------------------------------------
# PAINT CALCULATOR
#
# by | Oskar Garcia OG2236, in collaboration with Marni Rosenthal MAR2341 |
# Columbia University | ENGIE1006 | Spring 2019
# In-class problem set 1 – Problem 1 V.1.0
# V.1.0
# ______________________________________________________________________________


#
# -- Program greeting

print("\nHello! This program helps you calculate how\n"
      + "much paint you need to paint your room.\n"
      + "Please follow the instructions carefully\n")
#
# -- Query user for values and assign variables

paint_per_sqrM = 0.25  # -- The factor for paint per squared meter
height = float(input("Please type a number for the height of the room: "))
width = float(input("Please type a number for the width of the room: "))
length = float(input("Please type a number for the length of the room: "))

#
# -- Computations for the desired value

surface_area_sqrCm = (2 * (height * width)) + (2 * (height * length)) \
               + (width * length)
print(surface_area_sqrCm)

surface_area_sqrM = surface_area_sqrCm / 10000
print(surface_area_sqrM)

paint_volume = surface_area_sqrM * paint_per_sqrM

# -- Display the desired volume

print("\nThe volume of paint you need is: ", paint_volume, "liters")
