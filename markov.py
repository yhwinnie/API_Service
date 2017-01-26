import re
import random

def read(source):
    tokens = split_on_white_space(source)
    return tokens

def split_on_white_space(text):
    encoded_text = text.decode('unicode_escape').encode('ascii','ignore')
    tokens = re.split('\s+', encoded_text)

    #markov_model(tokens)
    return tokens

def histogram(tokens):
    histogram_model = {}
    for token in tokens:
        if histogram_model == {}:
            histogram_model[token] = 1
        elif token in histogram_model:
            histogram_model[token] += 1
        else:
            histogram_model[token] = 1
    return histogram_model


def markov_model(tokens):
    histogram_model = histogram(tokens)
    dictionary = {}

    for index in range(len(tokens)):
        if index < len(tokens) - 2:
            tup = (tokens[index], tokens[index + 1])

            if tup not in dictionary:
                dictionary[tup] = {tokens[index + 2]: 1}
            elif tokens[index + 2] not in dictionary[tup]:
                dictionary[tup][tokens[index + 2]] = 1
            else:
                dictionary[tup][tokens[index + 2]] += 1
    return generate_sentences(dictionary)


def generate_sentences(dictionary):
    keys = dictionary.keys()
    random_key = random.choice(keys)

    lst = []
    while 'ENDEND' != random_key[0]:
        random_key = random.choice(keys)

    random_next = stochastic(dictionary[random_key])

    lst.append(random_key[1])
    lst.append(random_next)

    key = random_key[1]

    while random_next != 'ENDEND':

        val = (key, random_next)

        key = random_next
        random_next = stochastic(dictionary[val])

        lst.append(random_next)

    lst.append(" -- Barack Obama")

    text = ' '.join(lst).replace(" ENDEND", '.')
    print(text)

    return lst


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
    read(open("corpus_clean.txt").read())
