# ------------------------------------------------------------------------------
# K-SMALLEST NUMBERS
#
# by | Oskar Garcia OG2236 |
# Columbia University | ENGIE1006 | Spring 2019
# In-class Project 2 – Part 1
# V.1.0
# ______________________________________________________________________________


# -- Program greeting

print("\nHello! This program helps you find a list of\n"
      + "the k-smallest numbers within another list. \n"
      + "Please follow the instructions carefully.\n")

#
# -- Prompts the user and asks for a value for k

k_value = int(input("Please type how many least numbers you\n"
                    + "want from the given list: "))

#
# -- Defines selection sort upon the given list along with a function
#    called "slice" that returns the sub-list requested by the user


def find_min(the_list):

    current_index = 0
    current_item = the_list[current_index]
    counter = 0

    for item in the_list:
        if(current_item is None) or (item is not None and item < current_item):

            current_item = item
            current_index = counter
        counter += 1

    return current_index


def selection_sort(the_list):

    output_list = []  # -- The returned variable to hold the sublist

    for item in range(len(the_list)):
        location = find_min(the_list)
        value = the_list[location]
        output_list.append(value)
        the_list[location] = None

    return output_list


def slicer(the_list, upper_limit):

    return the_list[: upper_limit]


#
# -- Testing framework

test_input = [34, 95, 107, -895, 0, -1117]  # -- Change the values for testing

print("\nThe list you provided was:\n", test_input)

test_output = selection_sort(test_input)  # -- The sorted list

print("\nThe sublist you requested is:\n",
      slicer(test_output, k_value))  # -- Returns the specified substring
