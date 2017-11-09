from string import punctuation


def clean_up_words_from_file(file_name):
    """TODO: make list of words from text, input file name, and returns list of words."""
    new_word_list = []
    with open(file_name, 'r') as f:
        word_list = f.read().split()
    for word in word_list:
        if "--" in word:
            word_list.remove(word)
            word = word.split('--')
            for a_word in word:
                word_list.append(a_word)
        elif "-" in word:
            word_list.remove(word)
            word = word.split('-')
            for a_word in word:
                word_list.append(a_word)
    for word in word_list:
        clean_word = ''
        for c in word:
            if c not in punctuation:
                clean_word += c
        if clean_word.isalpha() is True and "http" not in clean_word:
            new_word_list.append(clean_word.lower())
    return new_word_list
