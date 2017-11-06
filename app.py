from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def hello_world(number_of_words=10):
    # return 'Hello, World!'
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

# def random_sentence(number_of_words=10):
#     with open("/usr/share/dict/words", 'r') as f:
#         words_list = f.read().split()
#
#     sentence = ""
#     for _ in range(0, number_of_words):
#         random_number = random.randint(0, len(words_list) - 1)
#         if sentence == "":
#             sentence = words_list[random_number]
#         else:
#             sentence += " " + words_list[random_number]
#     return(sentence)
