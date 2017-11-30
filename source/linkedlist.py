#!python
import time

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

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
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    # Build an iterator from scratch with __iter__() and __next__()
    def __iter__(self):
        """Return the iterator object itself"""
        self.node = self.head
        return self

    def __next__(self):
        """Return the current node in the sequence.
        On reaching the end, and in subsequent calls,
        it must raise StopIteration"""
        if self.node is not None:
            node = self.node
            # assign next node to self.node
            self.node = self.node.next
            return node
        else:
            raise StopIteration

    def items(self): # O(n) time/space
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        # node = self.head  # O(1) time to assign new variable
        # # Loop until node is None, which is one node too far past tail
        # while node is not None:  # Always n iterations because no early return
        #     items.append(node.data)  # O(1) time (on average) to append to list
        #     # Skip to next node to advance forward in linked list
        #     node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        for node in self: # O(n) time
            items.append(node.data) # O(1) space
        return items  # O(1) time to return list/O(n) space

    def is_empty(self): # O(1) time/space
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None # O(1) time/space

    def length(self): # O(n) time/O(1) space
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        length = 0 # O(1) time/space
        # node = self.head  # O(1) time to assign new variable
        # # Loop until node is None, which is one node too far past tail
        # while node is not None:  # O(n) time Always n iterations because no early return
        #     length += 1
        #     node = node.next  # O(1) time to reassign variable
        # # Now list contains items from all nodes
        # for _ in self:
        #     length += 1

        # alternative length calculation with items()
        length = len(self.items()) # O(n) time/ O(1) space

        return length  # O(1) time

    def append(self, item): # O(1) time/space
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        node = Node(item) # O(1) time/space
        # TODO: Append node after tail, if it exists
        if self.tail is None:
            self.head = node # O(1) time/space
            self.tail = node # O(1) time/space
        else:
            self.tail.next = node # O(1) time/space
            self.tail = node # O(1) time/space

    def prepend(self, item): # O(1) time/space
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        node = Node(item) # O(1) time/space
        # TODO: Prepend node before head, if it exists
        if self.is_empty():
            self.head = node # O(1) time/space
            self.tail = node # O(1) time/space
        else:
            node.next = self.head # O(1) time/space
            self.head = node # O(1) time/space

    def find(self, quality): # O(n) time/O(1) space
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        # node = self.head  # O(1) time to assign new variable
        # item = None
        # # Loop until node is None, which is one node too far past tail
        # while node is not None:  # Always n iterations because no early return
        #     if quality(node.data):
        #         item = node.data
        #         return item
        #     else:
        #         node = node.next
        for node in self: # best case running time: O(1), worst case running time: O(n)
            if quality(node.data):
                item = node.data # O(1) time/space
                return item # O(1) time/space

    def delete(self, item): # O(n) time/O(1) space
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        node = self.head  # O(1) time to assign new variable
        previous_node = None # O(1) time/space
        # Loop until node is None, which is one node too far past tail
        find_item = self.find(lambda item_: item_ == item) # O(n) time/O(1) space
        if find_item is None:
            raise ValueError('Item not found: {}'.format(item)) # O(1) time/space
        else:
            for node in self: # best case running time: O(1), worst case running time: O(n)
                if node == self.head:
                    if node.data == item:
                        self.head = node.next # O(1) time/space
                        if node == self.tail:
                            self.tail = previous_node # O(1) time/space
                        break
                    else:
                        previous_node = node # O(1) time/space
                else:
                    if node.data == item:
                        previous_node.next = node.next # O(1) time/space
                        if node == self.tail:
                            self.tail = previous_node # O(1) time/space
                        break
                    else:
                        previous_node = node # O(1) time/space
            # while node is not None:  # Always n iterations because no early return
            #     if node == self.head:
            #         if node.data == item:
            #             self.head = node.next
            #             if node == self.tail:
            #                 self.tail = previous_node
            #             break
            #         else:
            #             previous_node = node
            #             node = node.next
            #     else:
            #         if node.data == item:
            #             previous_node.next = node.next
            #             if node == self.tail:
            #                 self.tail = previous_node
            #             break
            #         else:
            #             previous_node = node
            #             node = node.next

    def replace(self, item, new_item): # O(n) time/O(1) space
        """Find a node whose data is item and replace it new item"""
        node = self.head # O(1) time/space
        find_item = self.find(lambda item_: item_ == item) # O(n) time/O(1) space
        if find_item is None:
            raise ValueError('Item not found: {}'.format(item))
        else:
            # while node is not None:
            #     if node.data == item:
            #         node.data = new_item
            #         break
            #     else:
            #         node = node.next
            if node.data == item:
                for node in self: # best case running time: O(1), worst case running time: O(n)
                    node.data = new_item # O(1) time/space
                    break


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    start_append_time = time.time()
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))
    end_append_time = time.time()
    elapsed_time = end_append_time - start_append_time
    print("elapsed time to append 3 items: {}".format(float(elapsed_time)))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    start_replace_time = time.time()
    ll.replace('A', 'D')
    end_replace_time = time.time()
    elapsed_time = end_replace_time - start_replace_time
    print("elapsed time to replace 1 item: {}".format(float(elapsed_time)))
    print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    ll.replace('D', 'A')
    print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        start_delete_time = time.time()
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))
        end_delete_time = time.time()
        elapsed_time = end_delete_time - start_delete_time
        print("elapsed time to delete 3 items: {}".format(float(elapsed_time)))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
