import re
from collections import defaultdict


dictionary = defaultdict(int)
def histogram(source_text):

    delimeters = ["\\", ",", ";", ":", "\n", "-", "!", "?", "(", ")", "'s", \
    "'\'", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "/", "}", "{"]

    f = open(source_text, 'r')
    lines = f.readlines()



    for line in lines:
        words = line.strip().translate(None, ''.join(delimeters)).split()
        for word in words:
            dictionary[word] += 1
    return dictionary


def unique_words(histogram):
    total = 0
    for (key, val) in histogram.iteritems():
        total += val
    return total


def frequency(word, histogram):
    return histogram[word]



if __name__ == '__main__':
    histogram_val = histogram("sherlock.rtf")
    print(histogram_val)
    print(unique_words(histogram_val))
    print(frequency("the", histogram_val))
