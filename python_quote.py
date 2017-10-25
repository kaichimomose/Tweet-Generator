import random

quotes = ["It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!"]


def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]


def reverse_sentense(quote):
    return quote[::-1]


def anagram_generator():
    return 0


if __name__ == '__main__':
    quote = random_python_quote()
    reverse_quote = reverse_sentense(quote)
    print(quote)
    print(reverse_quote)
