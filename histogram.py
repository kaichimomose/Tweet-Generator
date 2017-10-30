from collections import Counter
from string import punctuation

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
        clean_word = ''
        for c in word:
            if c not in punctuation:
                clean_word += c
        if "http" not in clean_word:
            new_word_list.append(clean_word)
    '''Counter(dictionary)'''
    # histogram = Counter((word for word in new_word_list if word.isalpha() is True))
    '''dictionary'''
    # histogram = {}
    # for word in new_word_list:
    #     if word.isalpha() is True:
    #         if word not in histogram:
    #             histogram[word] = 1
    #         else:
    #             histogram[word] += 1
    '''list of lists'''
    # unique_words_list = []
    # histogram = []
    # for word in new_word_list:
    #     if word.isalpha() is True:
    #         if word not in unique_words_list:
    #             unique_word = [word, 1]
    #             unique_words_list.append(word)
    #             histogram.append(unique_word)
    #         else:
    #             for i in range(0, len(histogram)):
    #                 if word == histogram[i][0]:
    #                     histogram[i][1] += 1
    '''list of tuples'''
    # unique_words_list = []
    # histogram = []
    # for word in new_word_list:
    #     if word.isalpha() is True:
    #         if word not in unique_words_list:
    #             unique_word = word, 1
    #             unique_words_list.append(word)
    #             histogram.append(unique_word)
    #         else:
    #             for i in range(0, len(histogram)):
    #                 if word == histogram[i][0]:
    #                     list_tuple = list(histogram[i])
    #                     list_tuple[1] += 1
    #                     histogram[i] = tuple(list_tuple)
    '''count'''
    unique_words_list = []
    histogram = []
    for word in new_word_list:
        if word.isalpha() is True:
            if word not in unique_words_list:
                unique_words_list.append(word)
                number_word_list = [1, unique_words_list]
            else:
                pass
                # for i in range(0, len(histogram)):
                #     if word == histogram[i][0]:
                #         list_tuple = list(histogram[i])
                #         list_tuple[1] += 1
                #         histogram[i] = tuple(list_tuple)
    histogram.append(tuple(number_word_list))
    print(histogram)
    return histogram


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    '''list of lists'''
    for i in range(0, len(histogram)):
        if word == histogram[i][0]:
            return histogram[i][1]
    '''dictionary'''
    if word in histogram:
        return histogram[word]
    else:
        return 0


# histogram1 = [('one', 1), ('fish', 1), ('two', 1), ('red', 1), ('blue', 1)]
# for i in range(0, len(histogram1)):
#     if "fish" == histogram1[i][0]:
#         number = histogram1[i][1]
#         number += 1
#         histogram1[i].remove(histogram1[i][1])
#         print(histogram1[i])
#         print(number)

histogram = histogram("1661.txt")
unique_words = unique_words(histogram)
frequency = frequency("mystery", histogram)
print("unique_words, frequency")
print("%s, %s" % (unique_words, frequency))
