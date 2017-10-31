from collections import Counter
from string import punctuation
import time

# with open("1661.txt", 'r') as f:
#     wordsList = f.read().split()
#     # for line in f:
#     #     # clean = line.replace('\n', '')
#     #     # wordsList.append(clean)
#     #     source_text = ''.join(line)
# print(wordsList)

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
    # histogram = {}
    # for word in new_word_list:
    #     if word not in histogram:
    #         histogram[word] = 1
    #     else:
    #         histogram[word] += 1
    '''list of lists'''
    unique_words_list = []
    histogram = []
    for word in new_word_list:
        if word not in histogram:
            unique_word = [word, 1]
            # unique_words_list.append(word)
            histogram.append(unique_word)
        else:
            for list in histogram:
                if word == list[0]:
                    list[1] += 1
    '''list of tuples'''
    # for i in range(0, len(histogram)):
    #     histogram[i] = tuple(histogram[i])
    '''list of tuples'''
    # unique_words_list = []
    # histogram = []
    # for word in new_word_list:
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
    '''list of counts'''
    # apper_times = []
    # count = []
    # for word in histogram:
    #     number = histogram[word]
    #     if number not in apper_times:
    #         apper_times.append(number)
    #         number_list = (number, [word])
    #         count.append(number_list)
    #     else:
    #         for index in count:
    #             if number == index[0]:
    #                 index[1].append(word)
    # histogram = sorted(count)
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
    for index in histogram:
        with open('histogram_entries.txt', 'a') as f:
            f.write("%s %s\n" % (index[0], index[1]))
    '''list of counts'''
    # for index in histogram:
    #     for word in index[1]:
    #         with open('histogram_entries.txt', 'a') as f:
    #             f.write("%s %s\n" % (word, index[0]))


def unique_words(histogram):
    return len(histogram)
    '''list of counts'''
    # number_of_unique_words = 0
    # for index in histogram:
    #     number_of_unique_words += len(index[1])
    # return number_of_unique_words

def frequency(word, histogram):
    '''list of lists/tuples'''
    for index in histogram:
        if word == index[0]:
            return index[1]
    '''dictionary'''
    # if word in histogram:
    #     return histogram[word]
    # else:
    #     return 0
    '''list of counts'''
    # for index in histogram:
    #     if word in index[1]:
    #         return index[0]


# histogram1 = [('one', 1), ('fish', 1), ('two', 1), ('red', 1), ('blue', 1)]
# for i in range(0, len(histogram1)):
#     if "fish" == histogram1[i][0]:
#         number = histogram1[i][1]
#         number += 1
#         histogram1[i].remove(histogram1[i][1])
#         print(histogram1[i])
#         print(number)
if __name__ == "__main__":
    start_time = time.time()
    histogram = histogram("1661.txt")
    logger_read_easily(histogram)
    unique_words = unique_words(histogram)
    frequency = frequency("dog", histogram)
    print("unique_words, frequency")
    print("%s, %s" % (unique_words, frequency))
    end_time = time.time() - start_time
    print(float(end_time))
