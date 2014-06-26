from unittest import TestCase

from linked_lists.linkedlists import Node
from linked_lists.linkedlists import LinkedList


class TestLinkedLists(TestCase):
    def test_linked_list_add_one(self):
        linked_list = LinkedList()

        linked_list.add_first(Node(10, None))

        self.assertEqual(1, linked_list.count)
        self.assertIsNot(linked_list.head, None)
        self.assertIsNot(linked_list.tail, None)
        self.assertEqual(10, linked_list.head.value)

    def test_linked_list_add_multiple(self):
        linked_list = LinkedList()

        linked_list.add_first(Node(14))
        linked_list.add_first(Node(28))
        linked_list.add_first(Node(52))

        self.assertEqual(3, linked_list.count)
        self.assertEqual(14, linked_list.tail.value)
        self.assertEqual(52, linked_list.head.value)

    def test_list_add_two(self):
        linked_list = LinkedList()

        linked_list.add_first(Node(1))
        linked_list.add_first(Node(2))

        self.assertEqual(2, linked_list.count)
        self.assertEqual(2, linked_list.head.value)
        self.assertEqual(1, linked_list.tail.value)

    def test_list_empty_add_to_end_one(self):
        linked_list = LinkedList()

        linked_list.add_last(Node(1))

        self.assertEqual(1, linked_list.count)
        self.assertEqual(1, linked_list.head.value)
        self.assertEqual(1, linked_list.tail.value)

    def test_list_add_to_end_two(self):
        linked_list = LinkedList()

        linked_list.add_last(Node(3))
        linked_list.add_last(Node(115))

        self.assertEqual(2, linked_list.count)
        self.assertEqual(3, linked_list.head.value)
        self.assertEqual(115, linked_list.tail.value)

    def test_list_add_to_end_three(self):
        linked_list = LinkedList()

        linked_list.add_last(Node(3))
        linked_list.add_last(Node(115))
        linked_list.add_last(Node(135))

        self.assertEqual(3, linked_list.count)
        self.assertEqual(3, linked_list.deep_count())
        self.assertEqual(3, linked_list.head.value)
        self.assertEqual(135, linked_list.tail.value)

    def test_list_three_remove_first(self):
        linked_list = LinkedList()

        linked_list.add_last(Node(3))
        linked_list.add_last(Node(18))
        linked_list.add_last(Node(4))

        linked_list.remove_first()

        self.assertEqual(2, linked_list.count)
        self.assertEqual(2, linked_list.deep_count())
        self.assertEqual(18, linked_list.head.value)
        self.assertEqual(4, linked_list.tail.value)

    def test_list_two_remove_first(self):
        linked_list = LinkedList()

        linked_list.add_last(Node(18))
        linked_list.add_last(Node(4))

        linked_list.remove_first()

        self.assertEqual(1, linked_list.count)
        self.assertEqual(1, linked_list.deep_count())
        self.assertEqual(4, linked_list.head.value)
        self.assertEqual(4, linked_list.tail.value)

    def test_list_one_remove_first(self):
        linked_list = LinkedList()

        linked_list.add_first(Node(212))

        linked_list.remove_first()

        self.assertEqual(0, linked_list.count)
        self.assertEqual(0, linked_list.deep_count())
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_list_remove_first_no_items(self):
        linked_list = LinkedList()

        linked_list.remove_first()

        self.assertEqual(0, linked_list.count)
        self.assertEqual(0, linked_list.deep_count())
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_list_remove_last_three_items(self):
        linked_list = LinkedList()

        linked_list.add_last(Node(10))
        linked_list.add_last(Node(20))
        linked_list.add_last(Node(30))

        linked_list.remove_last()

        self.assertEqual(2, linked_list.count)
        self.assertEqual(10, linked_list.head.value)
        self.assertEqual(20, linked_list.tail.value)
        self.assertIsNone(linked_list.tail.next)

    def test_list_remove_last_two_items(self):
        linked_list = LinkedList()

        linked_list.add_last(Node(10))
        linked_list.add_last(Node(20))

        linked_list.remove_last()

        self.assertEqual(1, linked_list.count)
        self.assertEqual(10, linked_list.head.value)
        self.assertEqual(10, linked_list.tail.value)
        self.assertIsNone(linked_list.tail.next)

    def test_list_remove_last_one_items(self):
        linked_list = LinkedList()

        linked_list.add_last(Node(10))
        linked_list.remove_last()

        self.assertEqual(0, linked_list.count)
        self.assertEqual(0, linked_list.deep_count())
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_list_remove_last_no_items(self):
        linked_list = LinkedList()

        linked_list.remove_last()

        self.assertEqual(0, linked_list.count)
        self.assertEqual(0, linked_list.deep_count())
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_list_iterator_three_items(self):
        linked_list = LinkedList()

        linked_list.add_last(Node(11))
        linked_list.add_last(Node(21))
        linked_list.add_last(Node(31))

        count = sum(1 for n in linked_list)

        self.assertEqual(3, count)

    def test_list_iterator_zero_items(self):
        linked_list = LinkedList()

        count = sum(1 for n in linked_list)

        self.assertEqual(0, count)

    def test_list_iterator_one_item(self):
        linked_list = LinkedList()

        linked_list.add_last(Node(22))

        count = sum(1 for n in linked_list)

        self.assertEqual(1, count)