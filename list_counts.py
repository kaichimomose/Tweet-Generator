def make_list_counts(dictogram):
    """TODO: create list of counts type histogram, inputs list of words, returns histogram."""
    apper_times = []
    count = []
    for word in dictogram:
        number = dictogram[word]
        if number not in apper_times:
            apper_times.append(number)
            number_list = (number, [word])
            count.append(number_list)
        else:
            for index in count:
                if number == index[0]:
                    index[1].append(word)
    return sorted(count)
