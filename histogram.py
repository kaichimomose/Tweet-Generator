from collections import Counter
from string import punctuation
from dictogram import Dictogram
import time
import random
# random.seed(42)


def dictionary(words_list):
    """TODO: create dictionary type histogram, inputs list of words, returns histogram."""
    histogram = {}
    for word in words_list:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram


def list_of_lists(words_list):
    """TODO: create list of lists type histogram, inputs list of words, returns histogram."""
    unique_words_list = []
    histogram = []
    for word in words_list:
        if word not in unique_words_list:
            unique_word = [word, 1]
            unique_words_list.append(word)
            histogram.append(unique_word)
        else:
            number = unique_words_list.index(word)
            histogram[number][1] += 1
            # for list in histogram:
            #     if word == list[0]:
            #         list[1] += 1
    # sort list numerical order
    histogram.sort(key=lambda x: x[1])
    return histogram


def list_of_tuples(words_list):
    """TODO: create list of tuples type histogram, inputs list of words, returns histogram."""
    '''creat list of tuples from the scratch'''
    unique_words_list = []
    histogram = []
    for word in words_list:
        if word not in unique_words_list:
            unique_word = word, 1
            unique_words_list.append(word)
            histogram.append(unique_word)
        else:
            number = unique_words_list.index(word)
            list_tuple = list(histogram[number])
            list_tuple[1] += 1
            histogram[number] = tuple(list_tuple)
            # for i in range(0, len(histogram)):
            #     if word == histogram[i][0]:
            #         list_tuple = list(histogram[i])
            #         list_tuple[1] += 1
            #         histogram[i] = tuple(list_tuple)
    # sort list numerical order
    histogram.sort(key=lambda x: x[1])
    return histogram


def list_counts(words_list):
    """TODO: create list of counts type histogram, inputs list of words, returns histogram."""
    histogram = dictionary(words_list)
    frequencies = []
    count = []
    for word in histogram:
        frequency = histogram[word]
        if frequency not in frequencies:
            frequencies.append(frequency)
            frequency_list = (frequency, [word])
            count.append(frequency_list)
        else:
            number = frequencies.index(frequency)
            count[number][1].append(word)
            # for number, words in count:
            #     if frequency == number:
            #         words.append(word)
    return sorted(count)


def clean_up_words_from_file(file_name):
    """TODO: make list of words from text, input file name, and returns list of words."""
    new_word_list = []
    with open(file_name, 'r') as f:
        word_list = f.read().split()
    for word in word_list:
        if "--" in word:
            word_list.remove(word)
            word = word.split('--')
            for a_word in word:
                word_list.append(a_word)
        elif "-" in word:
            word_list.remove(word)
            word = word.split('-')
            for a_word in word:
                word_list.append(a_word)
    for word in word_list:
        clean_word = ''
        for c in word:
            if c not in punctuation:
                clean_word += c
        if clean_word.isalpha() is True and "http" not in clean_word:
            new_word_list.append(clean_word.lower())
    return new_word_list


def make_histogram(file_name):
    """TODO: make list of word and histgram, input file name, and return histogram."""
    word_list = clean_up_words_from_file(file_name)
    '''Counter(dictionary)'''
    # histogram = Counter((word for word in word_list))
    '''dictionary'''
    histogram = dictionary(word_list)
    '''list of lists'''
    # histogram = list_of_lists(word_list)
    '''list of tuples'''
    # histogram = list_of_tuples(word_list)
    '''list of counts'''
    # histogram = list_counts(word_list)
    '''Dictogram'''
    # histogram = Dictogram(word_list)
    return histogram


def logger_read_easily(histogram):
    """TODO: create logger file and write tokens of each word"""
    with open('histogram_entries.txt', 'w') as f:
        f.write("This is histogram entries\n")
    '''dictionary'''
    for word in histogram:
        with open('histogram_entries.txt', 'a') as f:
            f.write("%s %s\n" % (word, histogram[word]))
    '''list of lists/tuples'''
    # for index in histogram:
    #     with open('histogram_entries.txt', 'a') as f:
    #         f.write("%s %s\n" % (index[0], index[1]))
    '''list of counts'''
    # for index in histogram:
    #     for word in index[1]:
    #         with open('histogram_entries.txt', 'a') as f:
    #             f.write("%s %s\n" % (word, index[0]))


def unique_words(histogram):
    """TODO: count number of unique words, input histogram, and return histogram."""
    return len(histogram)
    '''list of counts'''
    # number_of_unique_words = 0
    # # for count_tuple in histogram:
    # #     count = count_tuple[0]
    # #     words = count_tuple[1]
    # #     # Alternative to above 2 lines
    # #     count, words = count_tuple
    # # Alternative to above for loop
    # for count, words in histogram:
    #     number_of_unique_words += len(words)
    # return number_of_unique_words


def frequency(word, histogram):
    """TODO: return frequency of specific word, input word and histogram"""
    '''list of lists/tuples'''
    # for index in histogram:
    #     if word == index[0]:
    #         return index[1]
    '''dictionary'''
    if word in histogram:
        return histogram[word]
    else:
        return 0
    '''list of counts'''
    # # for index in histogram:
    # #     if word in index[1]:
    # #         return index[0]
    # # Alternative to above for loop
    # for count, words in histogram:
    #     if word in words:
    #         return count


def count_total_tokens(histogram):
    """TODO: count total tokens, input histogram, and returns total tokens."""
    total_tokens = 0
    '''list of lists'''
    # for list in histogram:
    #     total_tokens += list[1]
    '''list of tuples'''
    # for word, frequency in histogram:
    #     total_tokens += frequency
    '''dictionary'''
    for word in histogram:
        total_tokens += histogram[word]
    '''list of counts'''
    # # for a_tuple in histogram:
    # #     total_tokens += a_tuple[0] * len(a_tuple[1])
    # # Alternative to above for loop
    # for count, words in histogram:
    #     total_tokens += count * len(words)

    return total_tokens


def probability(histogram):
    """TODO: What it does, what input it takes, and what it returns."""
    total_tokens = count_total_tokens(histogram)
    tokens = []
    '''list of lists'''
    # for list in histogram:
    #     tokens.append(list[1])
    '''list of tuples'''
    # for word, frequency in histogram:
    #     tokens.append(frequency)
    '''list of counts'''
    # # for a_tuple in histogram:
    # #     tokens.append(a_tuple[0] * len(a_tuple[1]))
    # # Alternative to above for loop
    # for count, words in histogram:
    #     tokens.append(count * len(words))

    # probabilities = []
    # sum_probabilities = 0
    # for number in tokens:
    #     sum_probabilities += number/total_tokens
    #     probabilities.append(sum_probabilities)

    '''dictionary'''
    probabilities = {}
    sum_probabilities = 0
    for word in histogram:
        sum_probabilities += histogram[word]/total_tokens
        probabilities[sum_probabilities] = word

    return probabilities


def probability_of_word(word, histogram):
    total_tokens = count_total_tokens(histogram)
    '''list of lists'''
    # for list in histogram:
    #     if word in list:
    #         probability = list[1]/total_tokens * 100
    '''list of tuples'''
    # for a_word, frequency in histogram:
    #     if word == a_word:
    #         probability = frequency/total_tokens * 100
    '''dictionary'''
    for a_word in histogram:
        if word == a_word:
            probability = histogram[a_word]/total_tokens * 100
    '''list of counts'''
    # for count, words in histogram:
    #     if word in words:
    #         probability = count/total_tokens * 100

    return probability


'''dictionary'''
def pick_word(histogram):
    probabilities = probability(histogram)
    random_number = random.random()
    for a_probability in probabilities:
        if random_number < a_probability:
            picked_word = probabilities[a_probability]
            return picked_word
        else:
            pass


# def pick_word(histogram):
#     """TODO: What it does, what input it takes, and what it returns (if anything)."""
#     probabilities = probability(histogram)
#     random_number = random.random()
#     for i in range(0, len(probabilities)):
#         if random_number < probabilities[i]:
#             '''list of lists/tuples'''
#             picked_word = histogram[i][0]
#             '''list of counts'''
#             # random_number = random.randint(0, len(histogram[i][1]) - 1)
#             # picked_word = histogram[i][1][random_number]
#
#             return picked_word
#         else:
#             pass
#         # print("%s, %s\%" % (picked_word, probability))


def pick_many_words(histogram, number_of_experiment):
    """TODO: What it does, what input it takes, and what it returns (if anything)."""
    picked_words = []
    for _ in range(0, number_of_experiment):
        picked_word = pick_word(histogram)
        picked_words.append(picked_word)
    return picked_words


def make_sentence(word_list):
    """TODO: What it does, what input it takes, and what it returns (if anything)."""
    sentence = " ".join(word_list)
    sentence += "."
    return sentence


def count_word(word_to_count, word_list):
    """TODO: What it does, what input it takes, and what it returns (if anything)."""
    count = 0
    for word in word_list:
        if word == word_to_count:
            count += 1
    print("count of {!r}: {}".format(word_to_count, count))
    return count


def probability_of_word_in_sample_list(word_to_count, word_list, number_of_experiment):
    """TODO: What it does, what input it takes, and what it returns (if anything)."""
    count = count_word(word_to_count, word_list)
    probability = count/number_of_experiment * 100
    print("{!r} occupies {}%% of {} sample words".format(word_to_count, probability, number_of_experiment))


def test_histogram(file_name, word="the", num_words=1):
    start_time = time.time()
    histogram = make_histogram(file_name)
    logger_read_easily(histogram)
    print('histogram:', histogram)

    # TODO: explain what the next 4 lines are doing
    # unique_words = unique_words(histogram)
    print("unique words: {}".format(unique_words(histogram)))
    # frequency = frequency(word, histogram)
    print("frequency of {!r}: {}".format(word, frequency(word, histogram)))

    build_histogram_time = time.time()
    elapsed_time = build_histogram_time - start_time
    print("elapsed time to build histogram: {}".format(float(elapsed_time)))

    # TODO: explain what the next 3 lines are doing
    print("calculating probabilities...")
    specific_probability = probability_of_word(word, histogram)
    print("probability of {!r}: {}%%".format(word, specific_probability))

    # TODO: calculating this number based on histogram
    # num_words = 108283  # Sherlock Holmes
    # num_words = 100  # fish example
    print("randomly sampling {} words...".format(num_words))
    word_list = pick_many_words(histogram, num_words)

    # TODO: explain what the next 2 lines are doing
    probability_of_word_in_sample_list(word, word_list, num_words)

    sampling_time = time.time()
    elapsed_time = sampling_time - build_histogram_time
    print("elapsed time to sample words: {}".format(float(elapsed_time)))

    sentence = make_sentence(word_list)
    print(sentence)
    return sentence


if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    if len(arguments) >= 1:
        file_name = arguments[0]
        if len(arguments) >= 2:
            word = arguments[1]
            if len(arguments) >= 3:
                number_of_words = int(arguments[2])
            else:
                number_of_words = 1
        else:
            word = 'the'
    else:
        file_name = "source-text/1661.txt"
    test_histogram(file_name, word, number_of_words)
