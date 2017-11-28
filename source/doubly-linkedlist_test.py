#!python

from doublylinkedlist import DoublyLinkedList, DoublyNode
import unittest


class NodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = DoublyNode(data)
        # Initializer should add instance properties
        assert node.data is data
        assert node.next is None

    def test_linking_nodes(self):
        node1 = DoublyNode('A')
        node2 = DoublyNode('B')
        node3 = DoublyNode('C')
        # Link nodes together
        node1.next = node2
        node2.next = node3
        # Node links should be transitive
        assert node1.next is node2  # One link
        assert node1.next.next is node3  # Two links


class LinkedListTest(unittest.TestCase):

    def test_init(self):
        dll = DoublyLinkedList()
        # Initializer should add instance properties
        assert dll.head is None  # First node
        assert dll.tail is None  # Last node

    def test_init_with_list(self):
        dll = DoublyLinkedList(['A', 'B', 'C'])
        # Initializer should append items in order
        assert dll.head.data == 'A'  # First item
        assert dll.tail.data == 'C'  # Last item

    def test_items_after_append(self):
        dll = DoublyLinkedList()
        assert dll.items() == []
        # Append should add new item to tail of list
        dll.append('A')
        assert dll.items() == ['A']
        dll.append('B')
        assert dll.items() == ['A', 'B']
        dll.append('C')
        assert dll.items() == ['A', 'B', 'C']

    def test_items_after_prepend(self):
        dll = DoublyLinkedList()
        assert dll.items() == []
        # Prepend should add new item to head of list
        dll.prepend('C')
        assert dll.items() == ['C']
        dll.prepend('B')
        assert dll.items() == ['B', 'C']
        dll.prepend('A')
        assert dll.items() == ['A', 'B', 'C']

    def test_length_after_append(self):
        dll = DoublyLinkedList()
        assert dll.length() == 0
        # Append should increase length
        dll.append('A')
        assert dll.length() == 1
        dll.append('B')
        assert dll.length() == 2
        dll.append('C')
        assert dll.length() == 3

    def test_length_after_prepend(self):
        dll = DoublyLinkedList()
        assert dll.length() == 0
        # Prepend should increase length
        dll.prepend('C')
        assert dll.length() == 1
        dll.prepend('B')
        assert dll.length() == 2
        dll.prepend('A')
        assert dll.length() == 3

    def test_length_after_append_and_prepend(self):
        dll = DoublyLinkedList()
        assert dll.length() == 0
        # Append and prepend should increase length
        dll.append('C')
        assert dll.length() == 1
        dll.prepend('B')
        assert dll.length() == 2
        dll.append('D')
        assert dll.length() == 3
        dll.prepend('A')
        assert dll.length() == 4

    def test_length_after_delete(self):
        dll = DoublyLinkedList(['A', 'B', 'C', 'D', 'E'])
        assert dll.length() == 5
        # Delete should decrease length
        dll.delete('A')
        assert dll.length() == 4
        dll.delete('E')
        assert dll.length() == 3
        dll.delete('C')
        assert dll.length() == 2
        dll.delete('D')
        assert dll.length() == 1
        dll.delete('B')
        assert dll.length() == 0

    def test_append(self):
        dll = DoublyLinkedList()
        # Append should always update tail node
        dll.append('A')
        assert dll.head.data == 'A'  # New head
        assert dll.tail.data == 'A'  # New tail
        dll.append('B')
        assert dll.head.data == 'A'  # Unchanged
        assert dll.tail.data == 'B'  # New tail
        dll.append('C')
        assert dll.head.data == 'A'  # Unchanged
        assert dll.tail.data == 'C'  # New tail

    def test_prepend(self):
        dll = DoublyLinkedList()
        # Prepend should always update head node
        dll.prepend('C')
        assert dll.head.data == 'C'  # New head
        assert dll.tail.data == 'C'  # New head
        dll.prepend('B')
        assert dll.head.data == 'B'  # New head
        assert dll.tail.data == 'C'  # Unchanged
        dll.prepend('A')
        assert dll.head.data == 'A'  # New head
        assert dll.tail.data == 'C'  # Unchanged

    def test_find(self):
        dll = DoublyLinkedList(['A', 'B', 'C'])
        assert dll.find(lambda item: item == 'B') == 'B'  # Match equality
        assert dll.find(lambda item: item < 'B') == 'A'  # Match less than
        assert dll.find(lambda item: item > 'B') == 'C'  # Match greater than
        assert dll.find(lambda item: item == 'X') is None  # No matching item

    def test_delete_with_3_items(self):
        dll = DoublyLinkedList(['A', 'B', 'C'])
        assert dll.head.data == 'A'  # First item
        assert dll.tail.data == 'C'  # Last item
        dll.delete('A')
        assert dll.head.data == 'B'  # New head
        assert dll.tail.data == 'C'  # Unchanged
        dll.delete('C')
        assert dll.head.data == 'B'  # Unchanged
        assert dll.tail.data == 'B'  # New tail
        dll.delete('B')
        assert dll.head is None  # No head
        assert dll.tail is None  # No tail
        # Delete should raise error if item was already deleted
        with self.assertRaises(ValueError):
            dll.delete('A')  # Item no longer in list
        with self.assertRaises(ValueError):
            dll.delete('B')  # Item no longer in list
        with self.assertRaises(ValueError):
            dll.delete('C')  # Item no longer in list

    def test_delete_with_5_items(self):
        dll = DoublyLinkedList(['A', 'B', 'C', 'D', 'E'])
        assert dll.head.data == 'A'  # First item
        assert dll.tail.data == 'E'  # Last item
        dll.delete('A')
        assert dll.head.data == 'B'  # New head
        assert dll.tail.data == 'E'  # Unchanged
        dll.delete('E')
        assert dll.head.data == 'B'  # Unchanged
        assert dll.tail.data == 'D'  # New tail
        dll.delete('C')
        assert dll.head.data == 'B'  # Unchanged
        assert dll.tail.data == 'D'  # Unchanged
        dll.delete('D')
        assert dll.head.data == 'B'  # Unchanged
        assert dll.tail.data == 'B'  # New tail
        dll.delete('B')
        assert dll.head is None  # No head
        assert dll.tail is None  # No tail

    def test_delete_with_item_not_in_list(self):
        dll = DoublyLinkedList(['A', 'B', 'C'])
        # Delete should raise error if item not found
        with self.assertRaises(ValueError):
            dll.delete('X')  # Item not found in list


if __name__ == '__main__':
    unittest.main()
