# ------------------------------------------------------------------------------
# POPULATION ESTIMATION
#
# by | Oskar Garcia OG2236, in collaboration with Marni Rosenthal MAR2341 |
# Columbia University | ENGIE1006 | Spring 2019
# In-class problem set 1 – Problem 3 V.1.0
# V.1.0
# ______________________________________________________________________________

#
# -- Program greeting

print("\nHello! This program helps you calculate\n"
      + "the estimated population growth given a\n"
      + "number of elapsed years.\n")

#
# -- Define the rate variables at units per n-seconds

birth_rate = 7
death_rate = 13
imm_rate = 35

#
# -- Conversion factor and computation for converting years into seconds

secs_per_yr = 31536000

#
# -- Current population variable

current_pop = 307357870

#
# -- Prompt for the number of elapsed years and conversion into seconds

yrs_elapsed = int(input("Please provide a whole number of elapsed\nyears"
                        " to calculate an estimate: "))
yrs_in_secs = yrs_elapsed * secs_per_yr

#
# -- Calculates the changes in population by category

new_births = yrs_in_secs // birth_rate
new_deaths = yrs_in_secs // death_rate
new_imm = yrs_in_secs // imm_rate

#
# -- Computes the population change upon the initial value

new_pop = (current_pop + new_births + new_imm) - new_deaths

#
# -- Displays the desired value
print("The estimated population after", yrs_elapsed, "years is\n", new_pop)
