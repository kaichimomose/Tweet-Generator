import random
random.seed()

wordsList = []
with open("/usr/share/dict/words", 'r') as f:
    for line in f:
        clean = line.replace('\n', '')
        wordsList.append(clean)

def anagram_generator():
    anagram_find = False
    find = False
    while anagram_find is False:
        random_number = random.randint(0, len(wordsList) - 1)
        selected_word = wordsList[random_number]
        original = selected_word
        number_of_characters = len(selected_word)
        while find is False:
            selected_word = original
            anagram = ""
            for i in range(0, number_of_characters):
                number = random.randint(0, len(selected_word) - 1)
                character = selected_word[number]
                anagram += character
                selected_word = selected_word[:number] + selected_word[number + 1:]
            if anagram != original:
                find = True
            else:
                find = False
        find = False
        if anagram in wordsList:
            print(original)
            break
        else:
            anagram_find = False
    return anagram

if __name__ == '__main__':
    anagram = anagram_generator()
    print(anagram)
