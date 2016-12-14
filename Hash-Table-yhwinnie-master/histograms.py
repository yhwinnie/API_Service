#!python


from __future__ import division, print_function
from hashtable import HashTable


class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            if item in self.keys():
                self[item] += 1
            else:
                self[item] = 1
                self.types += 1
            self.tokens += 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        if item in self.keys():
            return self[item]
        return 0


class Listogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Listogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            if self.__contains__(item):
                self[self._index(item)] = (item, self.count(item) + 1)
            else:
                self.append((item, 1))
                self.types += 1
            self.tokens += 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        for (key, val) in self:
            if key == item:
                return val
        return 0

    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False"""
        for (key, val) in self:
            if key == item:
                return True
        return False


    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None"""
        index = 0
        for (key, val) in self:
            if key == target:
                return index
            index += 1
        return None


class BNode(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))

class Binarytogram(object):
    def __init__(self, iterable):
        self.root = None
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.insert(self.root, item)
            node = BNode(item)

    def insert(self, root, item):
        node = BNode(item)
        if root is None:
            root = node
        elif root.data > item:
            return BNode(self.insert(root.left, item)
        else:
            self.insert(root.right, item)


def test_binarytogram(array):
    print('array:' , array)

    binary_tree = Binarytogram(array)
    print('binary:', binary_tree.root)



def test_histogram(text_list):
    print('text list:', text_list)

    hist_dict = Dictogram(text_list)
    print('dictogram:', hist_dict)

    hist_list = Listogram(text_list)
    print('listogram:', hist_list)


def read_from_file(filename):
    """Parse the given file into a list of strings, separated by seperator."""
    return file(filename).read().strip().split()


if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # exclude script name in first argument
    if len(arguments) == 0:
        # test hisogram on letters in a word
        word = 'abracadabra'
        test_histogram(word)
        print()
        # test hisogram on words in a sentence
        sentence = 'one fish two fish red fish blue fish'
        word_list = sentence.split()
        test_histogram(word_list)
        test_binarytogram([4, 5, 6, 7, 1, 2, 3, 8, 7])
    elif len(arguments) == 1:
        # test hisogram on text from a file
        filename = arguments[0]
        text_list = read_from_file(filename)
        test_histogram(text_list)

    else:
        # test hisogram on given arguments
        test_histogram(arguments)
