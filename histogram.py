from collections import Counter

with open("1661.txt", 'r') as f:
    wordsList = f.read().split()
    # for line in f:
    #     # clean = line.replace('\n', '')
    #     # wordsList.append(clean)
    #     source_text = ''.join(line)


def histogram(source_text):
    word_List = source_text.split()
    histogram = Counter(word_List)
    return histogram


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    else:
        return 0


histogram = histogram(source_text)
unique_words(histogram)
frequency("fish", histogram)
