from dictogram import Dictogram
import list_counts
import sentence
import sample
import random

class Second_Marcov(object):

    def __init__(self, word_list):
        self.states = self.create_states(word_list)
        self.states_lists_of_counts = self.create_states_lists_counts()

    def check_word_after_words(self, word_list):
        '''take word list, check word after word and create dictionary {word: [words after word]} '''
        word_after_dict = {}
        for i in range(-1, len(word_list)):
            #
            if i == -1:
                words = "START"
                word_after = word_list[0]
            elif i == 0:
                words = ("START", word_list[i])
                word_after = word_list[1]
            elif i == len(word_list)-1:
                words = (word_list[i-1], word_list[i])
                word_after = "STOP"
            else:
                words = (word_list[i-1], word_list[i])
                word_after = word_list[i+1]
            #
            if words not in word_after_dict:
                word_after_dict[words] = [word_after]
            else:
                word_after_dict[words].append(word_after)

        return word_after_dict

    def create_states(self, word_list):
        '''convert list of words after word to histogram of words after word {word: {word after word: tokens}}'''
        word_after_dict = self.check_word_after_words(word_list)
        states = {}
        for words in word_after_dict:
            states[words] = Dictogram(word_after_dict[words])
        return states

    def create_states_lists_counts(self):
        '''convert dictionary type of histogram to list of counts type of histogram {word: [(count, [words after word])]}'''
        states_lists_of_counts = {}
        for words in self.states:
            states_lists_of_counts[words] = list_counts.make_list_counts(self.states[words])
        return states_lists_of_counts

    def calculate_probabilities_dict(self):
        '''calculate probability of each word in each histogram'''
        probabilities_dict = {}
        for words in self.states_lists_of_counts:
            probabilities_dict[words] = sample.probability(self.states[words].tokens, self.states_lists_of_counts[words])
        return probabilities_dict

    def pick_word(self, words):
        '''pick one word that is after input word based on probabilities'''
        probabilities_dict = self.calculate_probabilities_dict()
        if words in probabilities_dict:
            probabilities = probabilities_dict[words]
            random_number = random.random()
            for i in range(0, len(probabilities)):
                if random_number < probabilities[i]:
                    random_number = random.randint(0, len(self.states_lists_of_counts[words][i][1]) - 1)
                    picked_word = self.states_lists_of_counts[words][i][1][random_number]
                    return picked_word
                else:
                    pass

    def pick_many_words(self):
        '''pick number_of_words words and return list of words, initial word is 'START' and stop picking words when picking 'STOP' '''
        picked_words = []
        words = "START"
        while words[1] is not "STOP":
            picked_word = self.pick_word(words)
            if picked_word is not "STOP":
                picked_words.append(picked_word)
            if words == "START":
                second = "START"
            else:
                first, second = words
            words = (second, picked_word)
        return picked_words

def main():
    fish_text = 'one fish two fish red fish blue fish'
    word_list = fish_text.split()
    second_markov = Second_Marcov(word_list)
    picked_words = second_markov.pick_many_words()
    made_sentence = sentence.make_sentence(picked_words)
    print(made_sentence)


if __name__ == "__main__":
    main()
