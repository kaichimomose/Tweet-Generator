import random


def probability(total_tokens, histogram):
    """TODO: What it does, what input it takes, and what it returns."""
    # total_tokens = count_total_tokens(histogram)
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


def pick_word(total_tokens, histogram):
    """TODO: What it does, what input it takes, and what it returns (if anything)."""
    probabilities = probability(total_tokens, histogram)
    random_number = random.random()
    for i in range(0, len(probabilities)):
        if random_number < probabilities[i]:
            random_number = random.randint(0, len(histogram[i][1]) - 1)
            picked_word = histogram[i][1][random_number]
            # probability = (probabilities[i] - probabilities[i-1])/len(histogram[i][1])
            return picked_word
        else:
            pass
        # print("%s, %s\%" % (picked_word, probability))


def pick_many_words(total_tokens, histogram, number_of_experiment):
    """TODO: What it does, what input it takes, and what it returns (if anything)."""
    picked_words = []
    for _ in range(0, number_of_experiment):
        picked_word = pick_word(total_tokens, histogram)
        picked_words.append(picked_word)
    return picked_words


if __name__ == "__main__":
    
