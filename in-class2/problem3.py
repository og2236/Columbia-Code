# ------------------------------------------------------------------------------
# FINDING SUB-SEQUENCES IN DNA STRINGS
#
# by | Oskar Garcia OG2236 |
# Columbia University | ENGIE1006 | Spring 2019
# In-class Project 2 – Part 3
# V.1.0
# ______________________________________________________________________________


#
# -- Program greeting

print("\nHello! This program helps you find sub-sequences\n"
      + "of nucleotides within a larger sequence\n"
      + "Please follow the instructions carefully.\n")

print("Please change the values in the testing variables,\n"
      + "and run the program again to check the results\n")


#
# -- Detects if a given sequence is present within a larger one. If true, it
#    returns the index of the first instance, otherwise returns -1


def find(sequence, sub):

    low = 0  # -- Lower sub-string bounds, inclusive
    high = len(sub)  # -- Upper sub-string bounds, not-inclusive
    maximum = len(sequence)  # -- Maximum traversal space, not inclusive

    target_index = -1  # -- The returned variable

    while high <= maximum:

        current_slice = sequence[low: high]

        if current_slice == sub:
            target_index = low
            return target_index

        else:
            low += 1
            high += 1

    return target_index


#
# -- Returns a list with the indexes of all instances, otherwise returns
#    an empty list

def find_multi(sequence, sub):

    low = 0  # -- Lower sub-string bounds, inclusive
    high = len(sub)  # -- Upper sub-string bounds, not-inclusive
    maximum = len(sequence)  # -- Maximum traversal space, not inclusive

    instances = []  # -- The returned variable

    while high <= maximum:

        current_slice = sequence[low: high]

        if current_slice == sub:
            instances.append(low)

        low += 1
        high += 1

    return instances


#
# -- Testing framework

host = "CGCGCGTTTTTGCG"  # -- "host" is the larger string,
target = "GCG" # --  "target" is the sub-string

print("The host sequence is: ", host)
print("The target sequence is: ", target)

test_number = find(host, target)
print("The index from 'find' is: ", test_number)

test_list = find_multi(host, target)
print("The list from 'find_multi' is: ", test_list)
