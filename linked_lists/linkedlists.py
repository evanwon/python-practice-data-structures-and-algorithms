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

    def __iter__(self):
        current = self.head

        while current is not None:
            yield current
            current = current.next

    def __len__(self):
        return self.count

    def __contains__(self, item):
        """ Returns true if the item's value is found in the list
        (Since the add functions take a value and create a node internally, we can only check
        if the list contains the value - the external caller doesn't have a reference to the nodes
        within the list)
        :param item: The Node whose value to seek
        :return: True if a Node with the corresponding value is found
        """
        current = self.head

        while current is not None:
            if current.value == item:
                return True
            current = current.next

        return False

    def add_first(self, value):
        """ Adds a value as the first Node in the list
        :param value: The value to add
        :return: None
        """
        node = Node(value)

        node.next = self.head
        self.head = node

        self.count += 1

        if self.tail is None:
            self.tail = self.head

    def add_last(self, value):
        """ Adds a Node as the last item in the list
        :param value: The value to add
        :return: None
        """

        node = Node(value)

        if self.count == 0:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

        self.count += 1

    def remove_first(self):
        """ Removes the first Node from the list
        :return: None
        """
        if self.count == 0:
            return

        self.head = self.head.next

        self.count -= 1

        if self.count == 0:
            self.tail = None

    def remove_last(self):
        """ Removes the last Node from the list
        :return: None
        """
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

    def remove_value(self, value, remove_only_first = True):
        """ Remove all Nodes with the provided value
        :param value: If a Node has this value, it will be removed
        :param remove_only_first: If True, only remove the first matching Node encountered. Otherwise,
        continue removing all nodes with the provided value.
        :return: None
        """

        current = self.head
        prev = None

        while current is not None:
            if current.value == value:
                if prev is None:
                    # case one: our previous node is none, which means we're at the start of the list
                    self.remove_first()
                else:
                    # case two: previous exists, so cut out current by setting prev's next to current's next
                    # if current was the tail, its next would be None, which works out just fine when setting prev's
                    # next to be None
                    prev.next = current.next

                    # if we removed the tail (and thus prev's next is None), make prev the tail
                    if current.next is None:
                        self.tail = prev

                    self.count -= 1

                if remove_only_first:
                    break

            # keep on movin' through the list
            prev = current
            current = current.next

    def clear(self):
        """
        :return: Remove all items from the list
        """
        # Thanks, garbage collector!
        self.head = None
        self.tail = None
        self.count = 0

    def deep_count(self):
        """ Iterates through the entire Linked List to perform a count of all Nodes in the list
        Note: Use count to get a simple count of all Nodes, maintained during add and remove functions
        :return: The number of Nodes in the Linked List
        """
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
