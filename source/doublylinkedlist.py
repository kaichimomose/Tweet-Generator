#!python


class DoublyNode(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'DoublyNode({!r})'.format(self.data)

class DoublyLinkedList(object):
    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' <-> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    # Build an iterator from scratch with __iter__() and __next__()
    def __iter__(self):
        """Return the iterator object itself"""
        self.node = self.head
        return self

    def __next__(self):
        """Return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration"""
        if self.node is not None:
            node = self.node
            # assign next node to self.node
            self.node = self.node.next
            return node
        else:
            raise StopIteration

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        for node in self:
            items.append(node.data)
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        length = 0
        length = len(self.items())
        return length  # O(1) time to return list

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        node = DoublyNode(item)
        # TODO: Append node after tail, if it exists
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        node = DoublyNode(item)
        # TODO: Prepend node before head, if it exists
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        for node in self:
            if quality(node.data):
                item = node.data
                return item

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        # Loop until node is None, which is one node too far past tail
        find_item = self.find(lambda item_: item_ == item)
        if find_item is None:
            raise ValueError('Item not found: {}'.format(item))
        else:
            for node in self:
                if node == self.head:
                    if node.data == item:
                        self.head = node.next
                        if node == self.tail:
                            self.tail = None
                        break
                else:
                    if node.data == item:
                        node.prev.next = node.next
                        if node == self.tail:
                            self.tail = node.prev
                        else:
                            node.next.prev = node.prev
                        break

    def replace(self, item, new_item):
        """Find a node whose data is item and replace it new item"""
        find_item = self.find(lambda item_: item_ == item)
        if find_item is None:
            raise ValueError('Item not found: {}'.format(item))
        else:
            for node in self:
                if node.data == item:
                    node.data = new_item
                    break

def test_doubly_linked_list():
    dll = DoublyLinkedList()
    print('list: {}'.format(dll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        dll.append(item)
        print('list: {}'.format(dll))

    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('length: {}'.format(dll.length()))

    dll.replace('A', 'D')
    print('list: {}'.format(dll))

    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('length: {}'.format(dll.length()))

    dll.replace('D', 'A')
    print('list: {}'.format(dll))

    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('length: {}'.format(dll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            dll.delete(item)
            print('list: {}'.format(dll))

        print('head: {}'.format(dll.head))
        print('tail: {}'.format(dll.tail))
        print('length: {}'.format(dll.length()))


if __name__ == '__main__':
    test_doubly_linked_list()
