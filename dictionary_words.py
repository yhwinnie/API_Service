import random
import sys
from time import time

start_time = time()
num_words = int(sys.argv[1])

f = open("/usr/share/dict/words", 'r')
lines = f.read().splitlines()
#f.close()

#rtn_lst = []
def original_dictionary_words():
    rtn_lst = [lines[random.randint(0, len(lines) - 1)] for index in range(num_words)]
    rtn = ' '.join(rtn_lst)

    return rtn

def dictionary_words():
    random_sample = random.sample(lines, num_words)
    rtn = ' '.join(random_sample)
    range(0, num_words)
    return rtn

if __name__ == '__main__':
    print(original_dictionary_words())
    print(time() - start_time)
    #nd_time = time()

    #print(vocabulary_game())

# for index in range(num_words):
#     rtn_lst.append(lines[random.randint(0, len(lines) - 1))
