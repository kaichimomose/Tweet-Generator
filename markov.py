from dictogram import Dictogram


def check_word_after_word(word_list):
    word_after_dict = {}
    for i in range(0, len(word_list)):
        word = word_list[i]
        if word not in word_after_dict:
            if i == len(word_list)-1:
                pass
            else:
                word_after_dict[word] = [word_list[i+1]]
        else:
            if i == len(word_list)-1:
                pass
            else:
                word_after_dict[word].append(word_list[i+1])
    return word_after_dict


def create_histograms(word_list):
    word_after_dict = check_word_after_word(word_list)
    histogram_dict = {}
    for word in word_after_dict:
        histogram_dict[word] = Dictogram(word_after_dict[word])
    return histogram_dict


# def create_sentense(word_list)


def main():
    fish_text = 'one fish two fish red fish blue fish'
    histogram_dict = create_histograms(fish_text.split())
    print(histogram_dict)


if __name__ == "__main__":
    main()
