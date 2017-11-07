from flask import Flask, render_template
import histogram
import random
app = Flask(__name__)
file_name = "source-text/1661.txt"
word = "the"


@app.route('/')
def generate_sentence():
    sentence = histogram.test_histogram(file_name, word)
    return render_template("home.html", something=sentence)


@app.route('/newsentence')
def generate_new_sentence():
    sentence = histogram.test_histogram(file_name, word)
    return render_template("home.html", something=sentence)

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


if __name__ == "__main__":
    app.run(debug=True)