import re
import sys


def read(source_text):
    f = open(source_text, 'r+b')
    text = f.read()
    #output_file = open('corpus.txt', 'w')
    output_file = open('corpus_clean.txt', 'w')

    output_file.write(regex_text(text))



def regex_text(text):
    clean_paranthesis = re.sub(r'\(.*\)+', '', text)

    clean_brackets = re.sub(r'\[.*\]+', '', clean_paranthesis)

    clean_number_with_paranthesis = re.sub(r'(\d)\)*', '', clean_brackets)

    clean_slashes = re.sub(r'/', '', clean_number_with_paranthesis)

    clean_random_text = re.sub(r'Complete Text', '', clean_slashes)

    return clean_random_text




if __name__ == '__main__':
    regex_result = read("corpus.txt")
    print(regex_result)
