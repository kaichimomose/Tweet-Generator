from collections import Counter
from string import punctuation
import time
import random
# random.seed(42)


def dictionary(words_list):
    """TODO: What it does, what input it takes, and what it returns."""
    histogram = {}
    for word in words_list:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram


def list_of_lists(words_list):
    """TODO: What it does, what input it takes, and what it returns."""
    unique_words_list = []
    histogram = []
    for word in words_list:
        if word not in unique_words_list:
            unique_word = [word, 1]
            unique_words_list.append(word)
            histogram.append(unique_word)
        else:
            for list in histogram:
                if word == list[0]:
                    list[1] += 1
    # sort list numerical order
    histogram.sort(key=lambda x: x[1])
    return histogram


def list_of_tuples(words_list):
    '''creat list of tuples from the scratch'''
    # unique_words_list = []
    # histogram = []
    # for word in words_list:
    #     if word not in unique_words_list:
    #         unique_word = word, 1
    #         unique_words_list.append(word)
    #         histogram.append(unique_word)
    #     else:
    #         for i in range(0, len(histogram)):
    #             if word == histogram[i][0]:
    #                 list_tuple = list(histogram[i])
    #                 list_tuple[1] += 1
    #                 histogram[i] = tuple(list_tuple)
    # # sort list numerical order
    # histogram.sort(key=lambda x: x[1])
    '''use list of lists to create list of tuples'''
    histogram = list_of_lists(words_list)
    for i in range(0, len(histogram)):
        histogram[i] = tuple(histogram[i])
    return histogram


def list_counts(words_list):
    """TODO: What it does, what input it takes, and what it returns."""
    histogram = dictionary(words_list)
    apper_times = []
    count = []
    for word in histogram:
        number = histogram[word]
        if number not in apper_times:
            apper_times.append(number)
            number_list = (number, [word])
            count.append(number_list)
        else:
            for index in count:
                if number == index[0]:
                    index[1].append(word)
    return sorted(count)


def clean_up_words_from_file(file_name):
    """TODO: What it does, what input it takes, and what it returns."""
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
    """TODO: What it does, what input it takes, and what it returns."""
    word_list = clean_up_words_from_file(file_name)
    '''Counter(dictionary)'''
    # histogram = Counter((word for word in word_list))
    '''dictionary'''
    # histogram = dictionary(word_list)
    '''list of lists'''
    # histogram = list_of_lists(word_list)
    '''list of tuples'''
    # histogram = list_of_tuples(word_list)
    '''list of counts'''
    histogram = list_counts(word_list)
    return histogram


def logger_read_easily(histogram):
    """TODO: What it does, what input it takes, and what it returns."""
    with open('histogram_entries.txt', 'w') as f:
        f.write("This is histogram entries\n")
    '''dictionary'''
    # for word in histogram:
    #     with open('histogram_entries.txt', 'a') as f:
    #         f.write("%s %s\n" % (word, histogram[word]))
    '''list of lists/tuples'''
    # for index in histogram:
    #     with open('histogram_entries.txt', 'a') as f:
    #         f.write("%s %s\n" % (index[0], index[1]))
    '''list of counts'''
    for index in histogram:
        for word in index[1]:
            with open('histogram_entries.txt', 'a') as f:
                f.write("%s %s\n" % (word, index[0]))


def unique_words(histogram):
    """TODO: What it does, what input it takes, and what it returns."""
    # return len(histogram)
    '''list of counts'''
    number_of_unique_words = 0
    # for count_tuple in histogram:
    #     count = count_tuple[0]
    #     words = count_tuple[1]
    #     # Alternative to above 2 lines
    #     count, words = count_tuple
    # Alternative to above for loop
    for count, words in histogram:
        number_of_unique_words += len(words)
    return number_of_unique_words


def frequency(word, histogram):
    """TODO: What it does, what input it takes, and what it returns."""
    '''list of lists/tuples'''
    # for index in histogram:
    #     if word == index[0]:
    #         return index[1]
    '''dictionary'''
    # if word in histogram:
    #     return histogram[word]
    # else:
    #     return 0
    '''list of counts'''
    # for index in histogram:
    #     if word in index[1]:
    #         return index[0]
    # Alternative to above for loop
    for count, words in histogram:
        if word in words:
            return count


def count_total_tokens(histogram):
    """TODO: What it does, what input it takes, and what it returns."""
    total_tokens = 0
    '''list of counts'''
    # for a_tuple in histogram:
    #     total_tokens += a_tuple[0] * len(a_tuple[1])
    # Alternative to above for loop
    for count, words in histogram:
        total_tokens += count * len(words)
    return total_tokens


def probability(total_tokens, histogram):
    """TODO: What it does, what input it takes, and what it returns."""
    tokens = []
    # for a_tuple in histogram:
    #     tokens.append(a_tuple[0] * len(a_tuple[1]))
    # Alternative to above for loop
    for count, words in histogram:
        tokens.append(count * len(words))
    probabilities = []
    sum_probabilities = 0
    for number in tokens:
        sum_probabilities += number/total_tokens
        probabilities.append(sum_probabilities)
    return probabilities


def pick_word(histogram, probabilities):
    """TODO: What it does, what input it takes, and what it returns (if anything)."""
    random_number = random.random()
    for i in range(0, len(probabilities)):
        if i == 0:
            if random_number >= 0 and random_number < probabilities[i]:
                random_number = random.randint(0, len(histogram[i][1]) - 1)
                picked_word = histogram[i][1][random_number]
                # probability = probabilities[i]/len(histogram[i][1])
            else:
                pass
        else:
            if random_number >= probabilities[i-1] and random_number < probabilities[i]:
                random_number = random.randint(0, len(histogram[i][1]) - 1)
                picked_word = histogram[i][1][random_number]
                # probability = (probabilities[i] - probabilities[i-1])/len(histogram[i][1])
            else:
                pass
        # print("%s, %s\%" % (picked_word, probability))
    return picked_word


def pick_many_words(histogram, probabilities, number_of_experiment):
    """TODO: What it does, what input it takes, and what it returns (if anything)."""
    picked_words = []
    for _ in range(0, number_of_experiment):
        picked_word = pick_word(histogram, probabilities)
        picked_words.append(picked_word)
    return picked_words


def count_word(word_to_count, word_list):
    count = 0
    for word in word_list:
        if word == word_to_count:
            count += 1
    print("count of {!r}: {}".format(word_to_count, count))


def test_histogram(file_name, word):
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
    total_tokens = count_total_tokens(histogram)
    probabilities = probability(total_tokens, histogram)
    # TODO: calculating this number based on histogram
    # num_words = 108283  # Sherlock Holmes
    num_words = 10000  # fish example
    print("randomly sampling {} words...".format(num_words))
    word_list = pick_many_words(histogram, probabilities, num_words)

    # TODO: explain what the next 2 lines are doing
    count_word(word, word_list)
    # count_word("and", word_list)

    sampling_time = time.time()
    elapsed_time = sampling_time - build_histogram_time
    print("elapsed time to sample words: {}".format(float(elapsed_time)))


if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    if len(arguments) >= 1:
        file_name = arguments[0]
        if len(arguments) >= 2:
            word = arguments[1]
        else:
            word = 'the'
    else:
        file_name = "1661.txt"
    test_histogram(file_name, word)
