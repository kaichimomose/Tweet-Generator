import random, sys
import time


def random_sentence(number_of_words=1):
    with open("/usr/share/dict/words", 'r') as f:
        words_list = f.read().split()

    sentence = ""
    for _ in range(0, number_of_words):
        random_number = random.randint(0, len(words_list) - 1)
        if sentence == "":
            sentence = words_list[random_number]
        else:
            sentence += " " + words_list[random_number]
    return(sentence)


if __name__ == "__main__":
    start_time = time.time()
    params = sys.argv[1:]
    if len(params) == 1:
        number_of_words = int(params[0])
    else:
        number_of_words = 1
    sentence = random_sentence(number_of_words)
    print(sentence)
    end_time = time.time() - start_time
    print(float(end_time))
