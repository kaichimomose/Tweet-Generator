
class Node(object):

    def __init__(self):
        self.data = None
        self.pointer = None


class LinkedList(object):

    def __init__(self):
        """Initialize this histogram as a new list and count given words."""
        super(LinkedList, self).__init__()  # Initialize this as a new list
        self.head_pointer = 0
        self.head = Node()
        self.tail = Node()
        self[self.head_pointer] = self.head

    def append(self, data):
        for i in self:
            if self[i].data is None:
                self[i].data = data
                self[i].pointer = self.tail
            else:



def main():
    mylist = LinkedList()
    mylist.append('a')
    print('mylist.head.data: {}'.format(mylist.head.data))


if __name__ == "__main__":
    main()
