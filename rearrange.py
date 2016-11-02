import sys
import random


arr = []

def rearrange_words():
    arguments = sys.argv[1:]
    i = 0
    index_list = []
    while len(index_list) != len(arguments):
        rand_index = random.randint(0, len(arguments) - 1)
        if rand_index not in index_list:
            index_list.append(rand_index)
            get_word = arguments[rand_index]

            arr.append(get_word)

    print(', '.join(map(str, arr)))



if __name__ == '__main__':
    rearrange_words()
