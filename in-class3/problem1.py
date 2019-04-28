# ------------------------------------------------------------------------------
# COUNTING N-GRAMS
#
# by | Oskar Garcia OG2236 | Collabration with: Felipe dos Santos FD2437
# Columbia University | ENGIE1006 | Spring 2019
# In-class Project3 – V.1.0
# ______________________________________________________________________________

from collections import defaultdict
import string


#    HELPER FUNCTION
# -- Pre-processor takes in a .txt file and cleans it for further processing
def pre_processor(file_name):

    infile = open(file_name, 'r')
    raw_lines = infile.readlines()
    infile.close()

    #
    # -- Translates uppercase lines into a list of individual lowercase words
    dirty_words = []

    for line in raw_lines:
        temp_line = line.lower()
        temp_list = temp_line.split()
        dirty_words.extend(temp_list)

    #
    # -- Removes punctuation and extra characters from individual words
    clean_words = []

    for word in dirty_words:
        temp_word = word.strip(string.punctuation)
        clean_words.append(temp_word)

    return clean_words


#
# -- Builds list of n-sized tuples as n-grams
def count_ngrams(file_name, n=2):

    data_words = pre_processor(file_name)  # -- Acquires clean data
    ngram_dictionary = dict()

    back_index = 0  # -- Back index value for traversal
    front_index = n  # -- Front index value for traversal

    while front_index <= len(data_words):  # -- Populates the dictionary

        temp_tup = tuple(data_words[back_index:front_index])

        if temp_tup not in ngram_dictionary:
            ngram_dictionary[temp_tup] = 1
        else:
            ngram_dictionary[temp_tup] += 1

        back_index += 1
        front_index += 1

    return ngram_dictionary


#
# -- Returns tuples with single ocurrences
def single_occurrences(ngram_count_dict):

    ngram_dict = ngram_count_dict
    singles = []

    for ngram in ngram_dict:
        if ngram_dict[ngram] == 1:
            singles.append(ngram)

    return singles


#
# -- Returns the most frequent k ngrams in a dictionary
def most_frequent(ngram_count_dict, num=5):

    ngram_dict = ngram_count_dict
    unordered_list = []

    for ngram in ngram_dict:
        temp_pair = (ngram_dict[ngram], ngram)
        unordered_list.append(temp_pair)

    ordered_list = sorted(unordered_list, reverse=True)

    index = 0
    n_list = []

    if num <= len(ordered_list):
        while index < num:
            temp_pair = ordered_list[index]
            temp_tup = temp_pair[1]
            n_list.append(temp_tup)
            index += 1

    else:  # -- Returns entire list if num > list length – by Prof. Bauer
        for item in ordered_list:
            temp_tup = item[1]
            n_list.append(temp_tup)

    return n_list


def main():
    filename = 'alice.txt'
    n = 2
    most_frequent_k = 5

    ngram_counts = count_ngrams(filename, n)

    print('{}-grams that occur only once:'.format(n))
    print(single_occurrences(ngram_counts))

    print('{} most frequent {}-grams:'.format(most_frequent_k, n))
    print(most_frequent(ngram_counts, most_frequent_k))


if __name__ == "__main__":
    main()
