# ------------------------------------------------------------------------------
# PIG LATIN
#
# by | Oskar Garcia OG2236 |
# Columbia University | ENGIE1006 | Spring 2019
# In-class Project 2 – Part 2
# V.1.0
# ______________________________________________________________________________


# -- Program greeting

print("\nHello! This program helps you translate a word\n"
      + "into its Pig Latin counterpart.\n"
      + "Please follow the instructions carefully.\n")


#
# -- Defines the set of vowels as a global variable

vowels = ["a", "e", "i", "o", "u"]


#
# -- This function checks if a list contains a vowel as its initial character


def is_first_vowel(a_list):

    for letter in vowels:
        if letter is a_list[0]:  # -- Returns True if first character is a vowel
            return True
    return False  # -- Returns False if first character is not a vowel


#
# -- Converts the word string into a list and translates it by checking
#    the input for the three possible cases, as specified


def piggify(word):

    new_word = ""  # -- Empty string gets modified and returned as output
    word_list = list(word)  # -- Converts the string into a list of characters

    #
    # -- Case 1: Word starts with vowel
    if is_first_vowel(word_list):
        word_list.append("yay")
        new_word = new_word.join(word_list)
        return new_word

    #
    # -- Counts the number of vowels missing from the word

    counter = 0

    for letter in vowels:
        if letter not in word_list:
            counter += 1

    #
    # -- Case 2: Word has no vowels in it
    if counter == 5:
        word_list.append("ay")
        new_word = new_word.join(word_list)
        return new_word

    #
    # -- Case 3: Word starts with a consonant and has at least one vowel
    else:
        tail = []  # -- Collects the new tail letters for the word
        flag = True  # -- Controls while loop
        index = 0  # -- Tracks letter index

        while flag is True:

            if word_list[index] not in vowels:
                tail.append(word_list[index])
                index += 1

            else:
                flag = False  # -- Terminates loop at first vowel

        del word_list[:len(tail)]  # -- Deletes initial consonants
        word_list.extend(tail)  # -- Appends initial consonants to the word
        word_list.append("ay")
        new_word = new_word.join(word_list)
        return new_word


#
# -- This function runs the control flow and termination of the program

def controller():

    terminate = False
    terminator = "."

    while terminate is not True:

        user_word = input("Please type the word you want to translate\n"
                          + "or type a period if you want exit: ")

        if user_word is terminator:
            terminate = True
            print("\nSee you later!")

        else:
            print("\nYour word is: ", piggify(user_word), "\n")


#
# -- Runs the controller function to execute the program

controller()
