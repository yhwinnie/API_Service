#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes
        - Best case: omega(1) if nothing or one item in the linked list.
        - Worst case: O(n): Number of item in the list.
        """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count


    def append(self, item):
        """Insert the given item at the tail of this linked list
        - Best case: omega(1): Access the tail and input the item.
        - Worst case: O(1): Access the tail and input the item.
        """
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    def prepend(self, item):
        """Insert the given item at the head of this linked list
        - Best case: omega(1): Access the tail and input the item.
        - Worst case: O(1): Access the tail and input the item.
        """

        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self
            self.head = node


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError
        - Best case: omega(1): If the item is at the beginning of the list.
        - Worst case: O(n): Item is in the middle or the end of the list and
        have to travel the entire linkedlist to find it.
        """
        current = self.head
        previous = None

        if self.find(lambda item: current.data == item) == None:
            raise ValueError

        while current is not None:
            # Found an equal one
            if current.data == item:
                # Beginning of the list
                if previous is None:
                    # The only item in the list
                    if current.next is None:
                        self.tail = None
                    self.head = current.next
                    #current.next = None

                # The end of the list
                elif current.next is None:
                    self.tail = previous
                    self.tail.next = None
                    break
                else:
                    # The middle of the list
                    temp = current
                    current = current.next
                    temp.next = None
                    previous.next = current
                    break
                return current.data
            # Cannot find the item
            else:
                previous = current
                current = current.next


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality
        - Best case: omega(1): if the item is at the beginning of the linkedlist.
        - Worst case: O(n): If item is at the middle or end and need to
        traverse the entire linkedlist."""
        current = self.head
        while current is not None:
            if quality(current.data):
                return current.data
            current = current.next
        return None


def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    #print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    #print(ll.length())


if __name__ == '__main__':
    test_linked_list()
