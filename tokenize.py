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
    for index in range(len(tokens)):
        if index < len(tokens) - 1:
            if dictionary == {}:
                dictionary[(tokens[index], tokens[index + 1])] = 1
            elif (tokens[index], tokens[index + 1]) in dictionary:
                dictionary[(tokens[index], tokens[index + 1])] += 1
            else:
                dictionary[(tokens[index], tokens[index + 1])] = 1
    return dictionary

def markov_model(tokens):
    histogram_model = histogram(tokens)
    #print(histogram_model)
    dictionary = {}
    index = 0
    for index in range(len(tokens)):
        if index < len(tokens) - 2:
            tup = ((tokens[index], tokens[index + 1]), histogram_model[(tokens[index], tokens[index + 1])])
            if dictionary == {}:
                dictionary[tup] = {}
            elif tup not in dictionary:
                if (index + 3) < len(tokens):
                    word = (tokens[index + 2], tokens[index + 3])
                    dictionary[tup] = {word: 1}
                else:
                    word = (tokens[index + 2], tokens[index + 3])
                    if word in dictionary[tup]:
                        dictionary[tup][word] += 1
                    else:
                        dictionary[tup][word] = 1
    #print(dictionary)
    generate_sentences(dictionary, 7)
    return dictionary

def generate_sentences(dictionary, sentence_len):
    lst = []

    key = random.choice(dictionary.keys())
    key = key[0]
    lst.append(key[0])
    lst.append(key[1])

    for i in range(sentence_len):
        #print("KEY")
        #print(key)
        for (dict_key, val) in dictionary.iteritems():
            #print(dict_key)
            if dict_key[0] == key:
                #print("A match!")

                value_histogram = dictionary[dict_key]

                random_index = random_index_generator(value_histogram)
                key = stochastic(value_histogram)
                #print(key)
                lst.append(key[0].lower())
                lst.append(key[1].lower())
    #print(lst)
    lst.append('.')
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
