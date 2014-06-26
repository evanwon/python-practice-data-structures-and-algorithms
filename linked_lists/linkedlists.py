class Node:
    """ Defines a Node object with a value and a Next pointer
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """ Defines a Linked List object
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_first(self, node):
        node.next = self.head
        self.head = node

        self.count += 1

        if self.tail is None:
            self.tail = self.head

    def add_last(self, node):
        if self.count == 0:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

        self.count += 1

    def remove_first(self):
        if self.count == 0:
            return

        self.head = self.head.next

        self.count -= 1

        if self.count == 0:
            self.tail = None

    def remove_last(self):
        if self.count == 0:
            return

        if self.count == 1:
            self.tail = None
            self.head = None
        else:
            current = self.head

            while current.next != self.tail:
                current = current.next

            current.next = None
            self.tail = current

        self.count -= 1

    def remove(self, node):
        pass

    def find_node(self, node):
        pass

    def find_value(self, value):
        pass

    def enumerate(self):
        pass

    def deep_count(self):
        counter = 0

        current = self.head
        while current is not None:
            counter += 1
            current = current.next

        return counter


def print_nodes(head):
    while head is not None:
        print("Node value: ", head.Value)
        head = head.Next
