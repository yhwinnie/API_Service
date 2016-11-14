import sys
from collections import defaultdict
import random
from flask import Flask, request, url_for, jsonify
import json
import os

app = Flask(__name__)

@app.route('/<num_words>', methods=["GET"])
def readFiles(num_words):
    lst = []
    argument = "sherlock.rtf"

    f = open(argument, 'r')
    lines = f.readlines()

    num = 0

    while num < int(num_words):
        lst.append(stochastic(histogram(lines)))
        num += 1

    return ' '.join(lst)


def histogram(lines):
    dictionary = defaultdict(int)
    delimeters = ["\\", ",", ";", ":", "\n", "-", "!", "?", "(", ")", "'s", \
    "'\'", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "/", "}", "{"]

    for line in lines:
        words = line.strip().translate(None, ''.join(delimeters)).split()
        for word in words:
            dictionary[word] += 1
    return dictionary

# get the total amount of words in the histogram
# Add the total amount of prob, check if rand_index is <= prob_total
def random_index_generator(histogram):
    count = 0
    for (key, val) in histogram.iteritems():
        count += val
    random_index = random.randint(1, count)
    return random_index

def stochastic(histogram):
    random_index = random_index_generator(histogram)
    prob_total = 0
    for key, val in histogram.iteritems():
        prob_total += val
        if random_index <= prob_total:
            return key


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
