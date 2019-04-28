# ------------------------------------------------------------------------------
# 24-HOUR CLOCK
#
# by | Oskar Garcia OG2236, in collaboration with Marni Rosenthal MAR2341 |
# Columbia University | ENGIE1006 | Spring 2019
# In-class problem set 1 – Problem 2 V.1.0
# V.1.0
# ______________________________________________________________________________


#
# -- Program greeting

print("\nHello! This program helps you calculate\n"
      + "the time in a 24 hour format.\n"
      + "Please follow the instructions carefully\n")
#
# -- Conversion factors

one_hour = 3600
one_minute = 60

#
# -- Prompts the user for a value within the given range

prompt1 = "\nPlease provide a whole number of seconds \nbetween 1 and 86,400"\
          + " both inclusive: "
user_value = int(input(prompt1))

#
# -- Converts the user's input into the desired values

hours = (user_value // one_hour)  # -- Get quotient by integer division
minutes = ((user_value % one_hour) // one_minute)  # -- Remainder by modulo
seconds = (user_value % one_minute)  # -- Remainder by modulo

#
# -- Displays the desired value and terminates

print("The time is: ", hours, " hr ", minutes, " min ", seconds,
      "sec")
