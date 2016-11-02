import sys
import random



arguments = sys.argv[1:]

def rearrange_words():
    result_arr = []
    index_list = []
    while len(index_list) != len(arguments):
        rand_index = random.randint(0, len(arguments) - 1)
        if rand_index not in index_list:
            index_list.append(rand_index)
            get_word = arguments[rand_index]

            result_arr.append(get_word)

    rtn = ', '.join(map(str, result_arr))
    return rtn



if __name__ == '__main__':
    print(rearrange_words())
