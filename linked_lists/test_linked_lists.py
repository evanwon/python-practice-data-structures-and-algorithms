from unittest import TestCase

from linked_lists.linkedlists import Node
from linked_lists.linkedlists import LinkedList


class TestLinkedLists(TestCase):
    def test__add_first__single_item(self):
        ll = LinkedList()

        ll.add_first(10)

        self.assertEqual(1, ll.count)
        self.assertIsNotNone(ll.head)
        self.assertIsNotNone(ll.tail)
        self.assertEqual(10, ll.head.value)

    def test__add_first__multiple_items(self):
        ll = LinkedList()

        ll.add_first(14)
        ll.add_first(28)
        ll.add_first(52)

        self.assertEqual(3, ll.count)
        self.assertEqual(14, ll.tail.value)
        self.assertEqual(52, ll.head.value)

    def test__add_first__two_items(self):
        ll = LinkedList()

        ll.add_first(1)
        ll.add_first(2)

        self.assertEqual(2, ll.count)
        self.assertEqual(2, ll.head.value)
        self.assertEqual(1, ll.tail.value)

    def test__add_last__single_item(self):
        ll = LinkedList()

        ll.add_last(1)

        self.assertEqual(1, ll.count)
        self.assertEqual(1, ll.head.value)
        self.assertEqual(1, ll.tail.value)

    def test__add_last__two_items(self):
        ll = LinkedList()

        ll.add_last(3)
        ll.add_last(115)

        self.assertEqual(2, ll.count)
        self.assertEqual(3, ll.head.value)
        self.assertEqual(115, ll.tail.value)

    def test__add_last__three_items(self):
        ll = LinkedList()

        ll.add_last(3)
        ll.add_last(115)
        ll.add_last(135)

        self.assertEqual(3, ll.count)
        self.assertEqual(3, ll.deep_count())
        self.assertEqual(3, ll.head.value)
        self.assertEqual(135, ll.tail.value)

    def test__remove_first__with_three_items(self):
        ll = LinkedList()

        ll.add_last(3)
        ll.add_last(18)
        ll.add_last(4)

        ll.remove_first()

        self.assertEqual(2, ll.count)
        self.assertEqual(2, ll.deep_count())
        self.assertEqual(18, ll.head.value)
        self.assertEqual(4, ll.tail.value)

    def test__remove_first__with_two_items(self):
        ll = LinkedList()

        ll.add_last(18)
        ll.add_last(4)

        ll.remove_first()

        self.assertEqual(1, ll.count)
        self.assertEqual(1, ll.deep_count())
        self.assertEqual(4, ll.head.value)
        self.assertEqual(4, ll.tail.value)

    def test__remove_first__one_item(self):
        ll = LinkedList()

        ll.add_first(212)

        ll.remove_first()

        self.assertEqual(0, ll.count)
        self.assertEqual(0, ll.deep_count())
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test__remove_first__no_items(self):
        ll = LinkedList()

        ll.remove_first()

        self.assertEqual(0, ll.count)
        self.assertEqual(0, ll.deep_count())
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test__remove_last__with_three_items(self):
        ll = LinkedList()

        ll.add_last(10)
        ll.add_last(20)
        ll.add_last(30)

        ll.remove_last()

        self.assertEqual(2, ll.count)
        self.assertEqual(10, ll.head.value)
        self.assertEqual(20, ll.tail.value)
        self.assertIsNone(ll.tail.next)

    def test__remove_last__with_two_items(self):
        ll = LinkedList()

        ll.add_last(10)
        ll.add_last(20)

        ll.remove_last()

        self.assertEqual(1, ll.count)
        self.assertEqual(10, ll.head.value)
        self.assertEqual(10, ll.tail.value)
        self.assertIsNone(ll.tail.next)

    def test__remove_last__with_one_item(self):
        ll = LinkedList()

        ll.add_last(10)
        ll.remove_last()

        self.assertEqual(0, ll.count)
        self.assertEqual(0, ll.deep_count())
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test__remove_last__with_no_items(self):
        ll = LinkedList()

        ll.remove_last()

        self.assertEqual(0, ll.count)
        self.assertEqual(0, ll.deep_count())
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test__iterator__with_three_items(self):
        ll = LinkedList()

        ll.add_last(11)
        ll.add_last(21)
        ll.add_last(31)

        count = sum(1 for n in ll)

        self.assertEqual(3, count)
        # Verify our head and tail haven't changed
        self.assertEqual(11, ll.head.value)
        self.assertEqual(31, ll.tail.value)

    def test__iterator__with_zero_items(self):
        ll = LinkedList()

        count = sum(1 for _ in ll)

        self.assertEqual(0, count)

    def test__iterator__with_one_item(self):
        ll = LinkedList()

        ll.add_last(22)

        count = sum(1 for n in ll)

        self.assertEqual(1, count)
        # Verify our head and tail haven't changed
        self.assertEqual(22, ll.head.value)
        self.assertEqual(22, ll.tail.value)
        
    def test__remove_value__remove_middle(self):
        ll = LinkedList()
        
        ll.add_last(15)
        ll.add_last(5)
        ll.add_last(215)
        
        ll.remove_value(5)
        
        self.assertEqual(2, ll.count)
        self.assertEqual(15, ll.head.value)
        self.assertEqual(215, ll.tail.value)

        self.assertIsNotNone(ll.head)
        self.assertIsNotNone(ll.tail)
        self.assertIsNone(ll.tail.next)
        
    def test__remove_value__remove_end(self):
        ll = LinkedList()
        
        ll.add_last(15)
        ll.add_last(5)
        ll.add_last(5)
        ll.add_last(215)
        
        ll.remove_value(215)
        
        self.assertEqual(3, ll.count)
        self.assertEqual(15, ll.head.value)
        self.assertEqual(5, ll.tail.value)   
        self.assertIsNone(ll.tail.next)   

    def test__remove_value__remove_first(self):
        ll = LinkedList()
        
        ll.add_last(15)
        ll.add_last(5)
        ll.add_last(215)
        
        ll.remove_value(15)
        
        self.assertEqual(2, ll.count)
        self.assertEqual(5, ll.head.value)
        self.assertEqual(215, ll.tail.value)        

        self.assertIsNotNone(ll.head)
        self.assertIsNotNone(ll.tail)
        self.assertIsNone(ll.tail.next)
        
    def test__remove_value__remove_only_element(self):
        ll = LinkedList()
        
        ll.add_last(15)
        
        ll.remove_value(15)
        
        self.assertEqual(0, ll.count)
        self.assertIsNone(ll.head)   
        self.assertIsNone(ll.tail)   
        
    def test__remove_value__remove_nonexistent_item_does_nothing(self):
        ll = LinkedList()
        
        ll.add_last(15)
        ll.add_last(5)
        ll.add_last(215)
        
        ll.remove_value(10)
        
        self.assertEqual(3, ll.count)
        self.assertEqual(15, ll.head.value)
        self.assertEqual(215, ll.tail.value)        

        self.assertIsNotNone(ll.head)
        self.assertIsNotNone(ll.tail)
        self.assertIsNone(ll.tail.next)

    def test__remove_value__no_items_does_nothing(self):
        ll = LinkedList()

        ll.remove_value(10)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test__remove_value__add_remove_add(self):
        ll = LinkedList()

        ll.add_last(45)
        ll.add_last(35)
        ll.remove_value(45)
        ll.add_last(75)

        self.assertEqual(2, ll.count)
        self.assertEqual(35, ll.head.value)
        self.assertEqual(75, ll.tail.value)

        self.assertIsNotNone(ll.head)
        self.assertIsNotNone(ll.tail)
        self.assertIsNone(ll.tail.next)

    def test__remove_value__remove_all_with_value(self):
        ll = LinkedList()

        ll.add_last(15)
        ll.add_last(5)
        ll.add_last(15)
        ll.add_last(215)
        ll.add_last(15)

        ll.remove_value(15, remove_only_first=False)

        self.assertEqual(2, ll.count)
        self.assertEqual(5, ll.head.value)
        self.assertEqual(215, ll.tail.value)

        self.assertIsNotNone(ll.head)
        self.assertIsNotNone(ll.tail)
        self.assertIsNone(ll.tail.next)

    def test__len__three_items(self):
        ll = LinkedList()

        ll.add_first(10)
        ll.add_first(20)
        ll.add_first(30)

        self.assertEqual(3, len(ll))

    def test__len__no_items(self):
        ll = LinkedList()

        self.assertEqual(0, len(ll))

    def test__contains__contains_value(self):
        ll = LinkedList()

        node1 = Node(30)
        node2 = Node(40)
        node3 = Node(88)

        ll.add_first(node1)
        ll.add_first(node2)
        ll.add_first(node3)

        result = node3 in ll

        self.assertTrue(result)

    def test__contains__does_not_contain_value(self):
        ll = LinkedList()

        node1 = Node(30)
        node2 = Node(40)
        node3 = Node(88)

        ll.add_first(node1)
        ll.add_first(node2)
        ll.add_first(node3)

        result = Node(300) in ll


        self.assertFalse(result)

    def test__contains__no_values__nothing_found(self):
        ll = LinkedList()

        result = Node(88) in ll

        self.assertFalse(result)

    def test__clear__three_value(self):
        ll = LinkedList()

        ll.add_first(100)
        ll.add_first(200)
        ll.add_first(300)

        ll.clear()

        self.assertEqual(0, ll.count)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test__clear__no_value(self):
        ll = LinkedList()

        ll.clear()

        self.assertEqual(0, ll.count)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)