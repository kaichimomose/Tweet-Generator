import random, sys

wordsList = []

with open("/usr/share/dict/words", 'r') as f:
    for line in f:
        clean = line.replace('\n', '')
        wordsList.append(clean)


def displaySentence(number_of_word=1):
    sentence = ""
    for i in range(0, number_of_word):
        random_number = random.randint(0, len(wordsList) - 1)
        if sentence == "":
            sentence = wordsList[random_number]
        else:
            sentence = sentence + " " + wordsList[random_number]
    return(sentence)


if __name__ == "__main__":
    params = sys.argv[1:]
    if len(params) == 1:
        number_of_word = int(params[0])
    else:
        number_of_word = 1
    sentence = displaySentence(number_of_word)
    print(sentence)
