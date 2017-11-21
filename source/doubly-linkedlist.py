from linkedlist import LinkedList, Node


class DoublyLinkedList(LinkedList):

    def __init__(self, items=None):
        LinkedList.__init__(self, items)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        node = Node(item)
        node.data = LinkedList(node.data)
        # TODO: Append node after tail, if it exists
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def length(self):
        columns = len(self.items())
        rows = 0
        for node in self:
            linkedlist = node.data
            row = len(linkedlist.items())
            if row > rows:
                rows = row
        return '{} by {} matrix'.format(rows, columns)


def test_doubly_linked_list():
    dll = DoublyLinkedList()
    print('list: {}'.format(dll))

    print('\nTesting append:')
    for item in [['A', 'B', 'C'], ['D', 'E', 'F']]:
        print('append({!r})'.format(item))
        dll.append(item)
        print('list: {}'.format(dll))

    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('length: {}'.format(dll.length()))


if __name__ == '__main__':
    test_doubly_linked_list()
