from unittest import TestCase

from linked_lists.linkedlists import Node
from linked_lists.linkedlists import LinkedList


class TestLinkedLists(TestCase):
    def test_linked_list_add_one(self):
        ll = LinkedList()

        ll.add_first(Node(10, None))

        self.assertEqual(1, ll.count)
        self.assertIsNot(ll.head, None)
        self.assertIsNot(ll.tail, None)
        self.assertEqual(10, ll.head.value)

    def test_linked_list_add_multiple(self):
        ll = LinkedList()

        ll.add_first(Node(14))
        ll.add_first(Node(28))
        ll.add_first(Node(52))

        self.assertEqual(3, ll.count)
        self.assertEqual(14, ll.tail.value)
        self.assertEqual(52, ll.head.value)

    def test_list_add_two(self):
        ll = LinkedList()

        ll.add_first(Node(1))
        ll.add_first(Node(2))

        self.assertEqual(2, ll.count)
        self.assertEqual(2, ll.head.value)
        self.assertEqual(1, ll.tail.value)

    def test_list_empty_add_to_end_one(self):
        ll = LinkedList()

        ll.add_last(Node(1))

        self.assertEqual(1, ll.count)
        self.assertEqual(1, ll.head.value)
        self.assertEqual(1, ll.tail.value)

    def test_list_add_to_end_two(self):
        ll = LinkedList()

        ll.add_last(Node(3))
        ll.add_last(Node(115))

        self.assertEqual(2, ll.count)
        self.assertEqual(3, ll.head.value)
        self.assertEqual(115, ll.tail.value)

    def test_list_add_to_end_three(self):
        ll = LinkedList()

        ll.add_last(Node(3))
        ll.add_last(Node(115))
        ll.add_last(Node(135))

        self.assertEqual(3, ll.count)
        self.assertEqual(3, ll.deep_count())
        self.assertEqual(3, ll.head.value)
        self.assertEqual(135, ll.tail.value)

    def test_list_three_remove_first(self):
        ll = LinkedList()

        ll.add_last(Node(3))
        ll.add_last(Node(18))
        ll.add_last(Node(4))

        ll.remove_first()

        self.assertEqual(2, ll.count)
        self.assertEqual(2, ll.deep_count())
        self.assertEqual(18, ll.head.value)
        self.assertEqual(4, ll.tail.value)

    def test_list_two_remove_first(self):
        ll = LinkedList()

        ll.add_last(Node(18))
        ll.add_last(Node(4))

        ll.remove_first()

        self.assertEqual(1, ll.count)
        self.assertEqual(1, ll.deep_count())
        self.assertEqual(4, ll.head.value)
        self.assertEqual(4, ll.tail.value)

    def test_list_one_remove_first(self):
        ll = LinkedList()

        ll.add_first(Node(212))

        ll.remove_first()

        self.assertEqual(0, ll.count)
        self.assertEqual(0, ll.deep_count())
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_list_remove_first_no_items(self):
        ll = LinkedList()

        ll.remove_first()

        self.assertEqual(0, ll.count)
        self.assertEqual(0, ll.deep_count())
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_list_remove_last_three_items(self):
        ll = LinkedList()

        ll.add_last(Node(10))
        ll.add_last(Node(20))
        ll.add_last(Node(30))

        ll.remove_last()

        self.assertEqual(2, ll.count)
        self.assertEqual(10, ll.head.value)
        self.assertEqual(20, ll.tail.value)
        self.assertIsNone(ll.tail.next)

    def test_list_remove_last_two_items(self):
        ll = LinkedList()

        ll.add_last(Node(10))
        ll.add_last(Node(20))

        ll.remove_last()

        self.assertEqual(1, ll.count)
        self.assertEqual(10, ll.head.value)
        self.assertEqual(10, ll.tail.value)
        self.assertIsNone(ll.tail.next)

    def test_list_remove_last_one_items(self):
        ll = LinkedList()

        ll.add_last(Node(10))
        ll.remove_last()

        self.assertEqual(0, ll.count)
        self.assertEqual(0, ll.deep_count())
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_list_remove_last_no_items(self):
        ll = LinkedList()

        ll.remove_last()

        self.assertEqual(0, ll.count)
        self.assertEqual(0, ll.deep_count())
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_list_iterator_three_items(self):
        ll = LinkedList()

        ll.add_last(Node(11))
        ll.add_last(Node(21))
        ll.add_last(Node(31))

        count = sum(1 for n in ll)

        self.assertEqual(3, count)
        # Verify our head and tail haven't changed
        self.assertEqual(11, ll.head.value)
        self.assertEqual(31, ll.tail.value)

    def test_list_iterator_zero_items(self):
        ll = LinkedList()

        count = sum(1 for n in ll)

        self.assertEqual(0, count)

    def test_list_iterator_one_item(self):
        ll = LinkedList()

        ll.add_last(Node(22))

        count = sum(1 for n in ll)

        self.assertEqual(1, count)
        # Verify our head and tail haven't changed
        self.assertEqual(22, ll.head.value)
        self.assertEqual(22, ll.tail.value)
        
    def test_list_remove_by_value(self):
        ll = LinkedList()
        
        ll.add(Node(15))
        ll.add(Node(5))
        ll.add(Node(215))
        
        ll.remove_by_value(5)
        
        self.assertEqual(2, ll.count)
        self.assertEqual(15, ll.head.value)
        self.assertEqual(215, ll.tail.value)