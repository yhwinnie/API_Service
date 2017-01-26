import re
import sys
import random



def read(source_text):
    f = open(source_text, 'r+b')
    text = f.read()
    output_file = open('corpus_clean.txt', 'w')

    # Clean corpus
    text = clean_corpus(text)

    tokenize(text)
    # Call markov model to generate sentences
    output_file.write(text)
    #markov_model(tokenize(text))

def clean_corpus(text):
    # remove punctuations
    punctuations = "!@#$%^&*~()//~`--"

    for punc in punctuations:
        text = text.replace(punc, '')

    # remove President Obama:
    text = text.replace("President Obama:", '')

    # remove 'hey'
    text = text.replace("Hey", '')

    # remove Questions asked by audience
    text = text.replace("Questions: [A-z ?]+", '')

    # Replace all dots with *END
    text = text.replace('.', ' ENDEND ')

    text = text.replace('U ENDEND S ENDEND', 'United States ')

    text = text.replace('U ENDEND N ENDEND', 'United Nations')

    text = text.replace('Mr ENDEND ', 'Mr.')


    return text


def tokenize(text):
    # To match beginning of a sentence and anything between until a .?, is reached

    # Match words with (and)[ A-z]+
    regex = re.compile("[^.?!](.*?)[.?!;]")
    regex_matches = regex.findall(text)

    tokens = []
    for match in regex_matches:
        tokens.append(match)

    #print(tokens)
    markov(tokens)
    return tokens

def markov(lst):
    tokens = []
    for sentence in lst:
        token = []
        for each_word in sentence.split():
            token.append(each_word)
        tokens.append(token)

    create_markov_model(tokens)

    return tokens

# Histogram (in each list there is a dictionary)
def histogram(tokens):
    histogram_model = {}
    for token in tokens:
        for word in token:
            if histogram_model == {}:
                histogram_model[word] = 1
            elif word in histogram_model:
                histogram_model[word] += 1
            else:
                histogram_model[word] = 1
    return histogram_model


def create_markov_model(tokens):
    histogram_model = histogram(tokens)
    markov_model = {}
    for sentence in tokens:
        for index in range(len(sentence)):
            if (index + 1) < len(sentence) - 1:
                word = sentence[index]
                following_word = sentence[index + 1]
                if word not in markov_model:
                    markov_model[word] = {}
                else:
                    markov_model[word][following_word] = histogram_model[following_word]

    print(markov_model)
    generate_tweet_sentences(markov_model)
    return markov_model

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


def generate_tweet_sentences(markov_model):
    keys = markov_model.keys()
    print(keys)
    random_key = random.choice(keys)
    lst = []

    i = 0
    while markov_model[random_key] != {}:
        #lst.append(random_key)
        #print(markov_model[random_key])
        lst.append(random_key)
        random_key = stochastic(markov_model[random_key])

        i+=1
    print(' '.join(lst))



if __name__ == '__main__':
    regex_result = read("corpus_clean copy.txt")
    #print(regex_result)
