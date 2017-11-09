from flask import Flask, render_template, request
from dictogram import Dictogram
import list_counts
import sentence
import sample
import cleanup

app = Flask(__name__)
file_name = "source-text/1661.txt"
word = "the"
word_list = cleanup.clean_up_words_from_file(file_name)


@app.route('/')
def generate_sentence():
    number_of_words = request.args.get('num', default=10, type=int)
    histogram = Dictogram(word_list)
    histogram_list_counts = list_counts.make_list_counts(histogram)
    picked_words = sample.pick_many_words(histogram.tokens, histogram_list_counts, number_of_words)
    made_sentence = sentence.make_sentence(picked_words)
    return render_template("home.html", something=made_sentence)


@app.route('/newsentence')
def generate_new_sentence():
    number_of_words = request.args.get('num', default=10, type=int)
    histogram = Dictogram(word_list)
    histogram_list_counts = list_counts.make_list_counts(histogram)
    picked_words = sample.pick_many_words(histogram.tokens, histogram_list_counts, number_of_words)
    made_sentence = sentence.make_sentence(picked_words)
    return render_template("home.html", something=made_sentence)

# Url Decoding
# import urlparse
# url_params = "session_id=1234&input=Hello+World"
# params_dict = urlparse.parse_qsl(url_params)
# params = dict(params_dict)
# print params
# #  will print {"session_id":"1234","input":"Hello World"}


if __name__ == "__main__":
    app.run(debug=True)
