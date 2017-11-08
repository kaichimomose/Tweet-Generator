from flask import Flask, render_template, request
import histogram
import random
app = Flask(__name__)
file_name = "source-text/1661.txt"
word = "the"


@app.route('/')
def generate_sentence():
    number_of_words = request.args.get('num', default=1, type=int)
    sentence = histogram.test_histogram(file_name, word, number_of_words)
    return render_template("home.html", something=sentence)


@app.route('/newsentence')
def generate_new_sentence():
    sentence = histogram.test_histogram(file_name, word, 100)
    return render_template("home.html", something=sentence)

# Url Decoding
# import urlparse
# url_params = "session_id=1234&input=Hello+World"
# params_dict = urlparse.parse_qsl(url_params)
# params = dict(params_dict)
# print params
# #  will print {"session_id":"1234","input":"Hello World"}


if __name__ == "__main__":
    app.run(debug=True)
