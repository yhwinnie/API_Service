import sys


arguments = sys.argv[1:]



def reverse_words():
    reverse_list = []
    i = len(arguments) - 1
    while i >= 0:
        reverse_list.append(arguments[i])

        i -= 1
    rtn = ', '.join(map(str, reverse_list))
    return rtn

if __name__ == '__main__':
    print(reverse_words())
