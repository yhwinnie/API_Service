import sys


def mad_libs():
    
    sentence = "Nice to meet you, " + raw_input("Hello, what's your name?: ") + "."
    return sentence

if __name__ == '__main__':
    print(mad_libs())
