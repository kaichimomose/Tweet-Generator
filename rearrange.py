import random, sys


def rearrange(params):
    word_List = params
    length = len(params)
    rearrange_order = ""
    for i in range(0, length):
        number = random.randint(0, len(word_List)-1)
        if rearrange_order == "":
            rearrange_order = word_List[number]
        else:
            rearrange_order += " " + word_List[number]
        word_List.remove(word_List[number])
    return rearrange_order


if __name__ == '__main__':
    params = sys.argv[1:]
    rearrange = rearrange(params)
    print(rearrange)
