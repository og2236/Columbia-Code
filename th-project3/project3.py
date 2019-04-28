# ------------------------------------------------------------------------------
# FARMERS MARKET DATABASE
#
# by | Oskar Garcia OG2236 |
# Columbia University | ENGIE1006 | Spring 2019
# Project3 – V.1.0
# ______________________________________________________________________________

# ------------------------------------------------------------------------------
# IMPORTANT: Please notice how I've cleaned the data starting from line 75
# ------------------------------------------------------------------------------

import string  # -- Allowed according to piazza


#    HELPER METHOD 1
# -- Iterates through a list of tuples and returns a dictionary with (k:v)
#    pairs of the form (zipcode : list of market tuples)
def zip_to_markets(list_of_tuples):

    dictionary = dict()

    for element in list_of_tuples:

        the_zipcode = element[4]

        if the_zipcode not in dictionary:
            dictionary[the_zipcode] = [element]  # -- New zipcode
        else:
            dictionary[the_zipcode].append(element)  # -- Known zipcode

    return dictionary


#    HELPER METHOD 2
# -- Iterates through a list of tuples and returns a dictionary with (k:v)
#    pairs of the form (city : set of zipcodes)
def city_to_zips(list_of_tuples):

    dictionary = dict()

    for element in list_of_tuples:

        city = element[3]
        if city not in dictionary:
            dictionary[city] = {element[4]}  # -- New city name
        else:
            dictionary[city].add(element[4])  # -- Known city name

    return dictionary


def read_markets(filename):
    """
    Read in the farmers market data from the file named filename and return 
    a tuple of two objects:
    1) A dictionary mapping zip codes to lists of farmers market tuples.
    2) A dictionary mapping towns to sets of zip codes.
    """

    data_file = open(filename, "r")

    # -- Reads lines and stores them as strings in a list
    data_strings = data_file.readlines()
    data_file.close()

    # -- Converts line strings into substrings of individual values
    data_lists_raw = []

    for element in data_strings:
        temp = element.split('#')  # -- Splits values by given delimiter
        del temp[5:7]  # -- Removes longitude and latitude
        data_lists_raw.append(temp)

    # -- Removes incorect or incomplete entries from the data set
    data_lists_clean = []

    for element in data_lists_raw:
        if ('none' not in element and  # -- Removes entries with 'none'
                '' not in element and  # -- Removes entries with ''
                len(element[4]) == 5 and  # -- Removes zipcodes != 5 digits
                '/' not in element[3] and  # -- Removes city names with '\'
                ',' not in element[3]):  # -- Removes city names with ','

            element[3] = string.capwords(element[3])  # -- Capitalize city names
            data_lists_clean.append(element)

    # -- Converts the dataset into a list of individual tuples
    data_tuples = []

    for element in data_lists_clean:
        data_tuples.append(tuple(element))

    # -- Returns the required tuple by calling helper functions defined above
    return zip_to_markets(data_tuples), city_to_zips(data_tuples)


def print_market(market):
    """
    Returns a human-readable string representing the farmers market tuple
    passed to the market parameter.
    """

    market_info = "\n{0}\n{1}\n{2}, {3} {4}"
    return market_info.format(market[1], market[2],
                              market[3], market[0], market[4])


#
# -- Testing framework
if __name__ == "__main__":

    # This main program first reads in the markets.txt once (using the function
    # from part (a)), and then asks the user repeatedly to enter a zip code or
    # a town name (in a while loop until the user types "quit").

    FILENAME = "markets.txt"

    try: 
        zip_to_market, town_to_zips = read_markets(FILENAME)

        halt_flag = True  # -- Flag controls while loop execution

        print("\nHello! Welcome to the Farmer's Market Database\n")
        print("Please follow the instructions carefully.\n")

        while halt_flag:

            legend = '\nEnter a valid city name, zip code, or quit:\n'
            user_input = string.capwords(input(legend))

            if user_input in zip_to_market:

                market_list = zip_to_market[user_input]

                for a in market_list:
                    print(print_market(a))

            elif user_input in town_to_zips:

                zip_set = town_to_zips[user_input]

                for zipcode in zip_set:

                    market_list = zip_to_market[zipcode]

                    for a in market_list:
                        print(print_market(a))

            elif user_input.lower() == 'quit':

                halt_flag = False
                print('Good bye!')

            else:
                print('Not found! Please choose a valid input')

    except (FileNotFoundError, IOError): 
        print("Error reading {}".format(FILENAME))
