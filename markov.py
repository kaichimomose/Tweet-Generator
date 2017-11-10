from dictogram import Dictogram
import list_counts
import sentence
import sample
import random

def check_word_after_word(word_list):
    ''''''
    word_after_dict = {}
    for i in range(-1, len(word_list)):
        #
        if i == -1:
            word = "START"
            word_after = word_list[i+1]
        elif i == len(word_list)-1:
            word = word_list[i]
            word_after = "STOP"
        else:
            word = word_list[i]
            word_after = word_list[i+1]
        #
        if word not in word_after_dict:
            word_after_dict[word] = [word_after]
        else:
            word_after_dict[word].append(word_after)

    return word_after_dict


def create_histograms(word_list):
    word_after_dict = check_word_after_word(word_list)
    histograms = {}
    for word in word_after_dict:
        histograms[word] = Dictogram(word_after_dict[word])
    return histograms


def create_histogram_lists_counts(histograms):
    histogram_lists_counts = {}
    for word in histograms:
        histogram_lists_counts[word] = list_counts.make_list_counts(histograms[word])
    return histogram_lists_counts


def calculate_probabilities_dict(histograms, histogram_lists_counts):
    probabilities_dict = {}
    for word in histogram_lists_counts:
        probabilities_dict[word] = sample.probability(histograms[word].tokens, histogram_lists_counts[word])
    return probabilities_dict


def pick_word(histograms, histogram_lists_counts, word):
    probabilities_dict = calculate_probabilities_dict(histograms, histogram_lists_counts)
    if word in probabilities_dict:
        probabilities = probabilities_dict[word]
        random_number = random.random()
        for i in range(0, len(probabilities)):
            if random_number < probabilities[i]:
                random_number = random.randint(0, len(histogram_lists_counts[word][i][1]) - 1)
                picked_word = histogram_lists_counts[word][i][1][random_number]
                # probability = (probabilities[i] - probabilities[i-1])/len(histogram[i][1])
                return picked_word
            else:
                pass

def pick_many_words(histograms, histogram_lists_counts, number_of_words):
    picked_words = []
    word = "START"
    for _ in range(0, number_of_words):
        picked_word = pick_word(histograms, histogram_lists_counts, word)
        if picked_word == "STOP":
            break
        else:
            picked_words.append(picked_word)
            word = picked_word
    return picked_words


def main():
    fish_text = 'one fish two fish red fish blue fish'
    word_list = fish_text.split()
    histograms = create_histograms(word_list)
    histogram_lists_counts = create_histogram_lists_counts(histograms)
    picked_words = pick_many_words(histograms, histogram_lists_counts, 10)
    made_sentence = sentence.make_sentence(picked_words)
    print(made_sentence)


if __name__ == "__main__":
    main()
