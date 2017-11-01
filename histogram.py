from collections import Counter
from string import punctuation
import time
import random
random.seed(1)


def dictionary(words_list):
    histogram = {}
    for word in words_list:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram


def list_of_lists(words_list):
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


def histogram(source_text):
    file_name = source_text
    new_word_list = []
    with open(file_name, 'r') as f:
        word_List = f.read().split()
    for word in word_List:
        if "--" in word:
            word_List.remove(word)
            word = word.split('--')
            for a_word in word:
                word_List.append(a_word)
        elif "-" in word:
            word_List.remove(word)
            word = word.split('-')
            for a_word in word:
                word_List.append(a_word)
    for word in word_List:
        clean_word = ''
        for c in word:
            if c not in punctuation:
                clean_word += c
        if clean_word.isalpha() is True and "http" not in clean_word:
            new_word_list.append(clean_word.lower())
    '''Counter(dictionary)'''
    # histogram = Counter((word for word in new_word_list))
    '''dictionary'''
    # histogram = dictionary(new_word_list)
    '''list of lists'''
    # histogram = list_of_lists(new_word_list)
    '''list of tuples'''
    # histogram = list_of_tuples(new_word_list)
    '''list of counts'''
    histogram = list_counts(new_word_list)
    print(histogram)
    return histogram


def logger_read_easily(histogram):
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
    # return len(histogram)
    '''list of counts'''
    number_of_unique_words = 0
    for index in histogram:
        number_of_unique_words += len(index[1])
    return number_of_unique_words

def frequency(word, histogram):
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
    for index in histogram:
        if word in index[1]:
            return index[0]

def total_tokens(number_of_unique_words, histogram):
    total_tokens = 0
    for a_tuple in histogram:
        total_tokens += a_tuple[0] * len(a_tuple[1])
    return total_tokens


def probability(total_tokens, histogram):
    tokens = []
    for a_tuple in histogram:
        tokens.append(a_tuple[0] * len(a_tuple[1]))
    probabilities = []
    sum_probabilities = 0
    for number in tokens:
        sum_probabilities += number/total_tokens
        probabilities.append(sum_probabilities)
    return probabilities

def pick_word(histogram, probabilities, number_of_experiment):
    picked_words = []
    for _ in range(0, number_of_experiment):
        random_number = random.random()
        for i in range(0, len(probabilities)):
            if i == 0:
                if random_number >= 0 and random_number < probabilities[i]:
                    random_number = random.randint(0, len(histogram[i][1]) - 1)
                    pick_word = histogram[i][1][random_number]
                    probability = probabilities[i]/len(histogram[i][1])
                else:
                    pass
            else:
                if random_number >= probabilities[i-1] and random_number < probabilities[i]:
                    random_number = random.randint(0, len(histogram[i][1]) - 1)
                    pick_word = histogram[i][1][random_number]
                    probability = (probabilities[i] - probabilities[i-1])/len(histogram[i][1])
                else:
                    pass
        picked_words.append(pick_word)
        # print("%s, %spersent" % (pick_word, probability))
    i = 0
    for word in picked_words:
        if word == "author":
            i += 1
    print(i)

if __name__ == "__main__":
    start_time = time.time()
    histogram = histogram("1661.txt")
    logger_read_easily(histogram)
    unique_words = unique_words(histogram)
    frequency = frequency("the", histogram)
    total_tokens = total_tokens(unique_words, histogram)
    probabilities = probability(total_tokens, histogram)
    print("unique_words, frequency")
    print("%s, %s" % (unique_words, frequency))
    pick_word(histogram, probabilities, 108283)
    end_time = time.time() - start_time
    print(float(end_time))
