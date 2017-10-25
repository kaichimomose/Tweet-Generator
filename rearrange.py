import random, sys


def rearrange(word_1="a", word_2="b", word_3="c", word_4="d"):
    word_List = [word_1, word_2, word_3, word_4]
    rearrange_order = ""
    for i in range(0, 4):
        number = random.randint(0, len(word_List)-1)
        if rearrange_order == "":
            rearrange_order = word_List[number]
        else:
            rearrange_order = rearrange_order + " " + word_List[number]
        word_List.remove(word_List[number])
    return rearrange_order


if __name__ == '__main__':
    params = sys.argv[1:]
    word_1 = params[0]
    word_2 = params[1]
    word_3 = params[2]
    word_4 = params[3]
    rearrange = rearrange(word_1, word_2, word_3, word_4)
    print(rearrange)
