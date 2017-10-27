import random, sys
import time

# wordsList = []
#
# with open("/usr/share/dict/words", 'r') as f:
#     for line in f:
#         # clean = line.replace('\n', '')
#         # wordsList.append(clean)
#         wordsList = f.read().split()


def displaySentence(number_of_word=1):
    wordsList = []

    with open("/usr/share/dict/words", 'r') as f:
        for line in f:
            # clean = line.replace('\n', '')
            # wordsList.append(clean)
            wordsList = f.read().split()

    sentence = ""
    for i in range(0, number_of_word):
        random_number = random.randint(0, len(wordsList) - 1)
        if sentence == "":
            sentence = wordsList[random_number]
        else:
            sentence += " " + wordsList[random_number]
    return(sentence)


if __name__ == "__main__":
    start_time = time.time()
    params = sys.argv[1:]
    if len(params) == 1:
        number_of_word = int(params[0])
    else:
        number_of_word = 1
    sentence = displaySentence(number_of_word)
    print(sentence)
    end_time = time.time() - start_time
    print(float(end_time))
