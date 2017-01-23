import re
import random


def tokenize(text):
    tokens = split_on_white_space(text)
    return tokens

def split_on_white_space(text):
    encoded_text = text.decode('unicode_escape').encode('ascii','ignore')
    tokens = re.split('\s+', encoded_text)
    #histogram(tokens)
    markov_model(tokens)
    return tokens

def histogram(tokens):
    dictionary = {}
    for word in tokens:
        if dictionary == {}:
            dictionary[word] = 1
        elif word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

def markov_model(tokens):
    histogram_model = histogram(tokens)
    dictionary = {}
    index = 0
    for index in range(len(tokens)):
        tup = (tokens[index], histogram_model[tokens[index]])
        if dictionary == {}:
            dictionary[tup] = {}
        elif tup not in dictionary:
            if (index + 1) < len(tokens):
                word = tokens[index + 1]
                dictionary[tup] = {word: 1}
        else:
            word = tokens[index + 1]
            if word in dictionary[tup]:
                dictionary[tup][word] += 1
            else:
                dictionary[tup][word] = 1
    #for key, value in dictionary.items():
        #print("key: ", key)
        #print("value: ", value)
        #print('\n')
    generate_sentences(dictionary, 10)
    return dictionary

def generate_sentences(dictionary, sentence_len):
    lst = []
    #print(value_histogram)
    #for i in range(sentence_len):
    key = random.choice(dictionary.keys())
    key = key[0]
    lst.append(key)

    for i in range(sentence_len):
        #print(key)
        for (dict_key, val) in dictionary.iteritems():
            if dict_key[0] == key:
                #print(dict_key[0])
                #print("A match")
                value_histogram = dictionary[dict_key]
                #print(value_histogram)
        #print(key[0])
                #print(value_histogram)
                random_index = random_index_generator(value_histogram)
                key = stochastic(value_histogram)
                #print(key)

                lst.append(key)

    #print(stochastic(dictionary))
    #value_histogram = dictionary[key]
    print(' '.join(lst))
    return ' '.join(lst)


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
        #print(key, val)
        prob_total += val
        if random_index <= prob_total:
            return key


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        tokens = tokenize(source)
    else:
        print('No source text filename given as argument.')
