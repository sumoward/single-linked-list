"""
Brian Ward
25/06/2014
Test suite for Implementation of Single_Linked_List

Using any programming language you're comfortable with,
write the required class(es) to implement
a simple singly-linked list.

Write two functions to
reverse the order of a singly-linked list using your implementation.
You must provide:
1. An iterative reverse.
2. A recursive reverse.
3. A full suite of automated tests.

"""
import unittest
from lists import Single_Linked_List


class SLLTestCase(unittest.TestCase):

    def setUp(self):
        self.sll = Single_Linked_List()
        self.sll1 = Single_Linked_List()
        for x in range(1, 11):
            self.sll1.insert_end_of_list(x)
        self.sll2 = Single_Linked_List()
        for x in range(1, 11):
            self.sll2.insert_end_of_list(x)
        self.sll3 = Single_Linked_List()
        for x in range(11, 21):
            self.sll3.insert_end_of_list(x)
        self.sll4 = Single_Linked_List()
        self.node1 = self.sll4.insert_start_of_list('begin')
        self.node2 = self.sll4.insert_end_of_list('end')
        self.node3 = self.sll4.insert_node('mid', self.node1)

    def tearDown(self):
        pass

    def test__str__(self):
        self.assertEqual('[ begin mid end ]', self.sll4.__str__())
        self.assertEqual('[ 1 2 3 4 5 6 7 8 9 10 ]', self.sll1.__str__())
        self.assertEqual('[ 11 12 13 14 15 16 17 18 19 20 ]',
                          self.sll3.__str__())

    def test_isEmpty(self):
        self.assertEqual(0, len(self.sll))

    def test__len__(self):
        self.assertEqual(0, len(self.sll))
        node1 = self.sll.insert_start_of_list('begin')
        self.assertEqual(1, len(self.sll))
        self.sll.insert_end_of_list('end')
        self.assertEqual(2, len(self.sll))
        self.sll.insert_node('mid', node1)
        self.assertEqual(3, len(self.sll))

    def test_insert_end_of_list(self):
        for x in range(1, 11):
            self.sll.insert_end_of_list(x)
            self.assertEqual(x, self.sll.tail.store)
        self.assertEqual(10, len(self.sll))

    def test_insert_start_of_list(self):
        for x in range(1, 11):
            self.sll.insert_start_of_list(x)
            self.assertEqual(x, self.sll.head.store)
        self.assertEqual(10, len(self.sll))

    def test_insert_node(self):
        self.assertEqual(10, len(self.sll1))
        self.sll1.insert_node('a', self.sll1.tail)
        self.assertEqual('[ 1 2 3 4 5 6 7 8 9 10 a ]', self.sll1.__str__())
        self.assertEqual(11, len(self.sll1))
        node1 = self.sll1.insert_node('b', self.sll1.head)
        self.assertEqual('b', node1.__str__())
        self.assertEqual('[ 1 b 2 3 4 5 6 7 8 9 10 a ]', self.sll1.__str__())
        self.assertEqual(12, len(self.sll1))
        node2 = self.sll1.insert_node('c', node1)
        self.assertEqual('c', node2.__str__())
        self.assertEqual(13, len(self.sll1))
        self.assertEqual('[ 1 b c 2 3 4 5 6 7 8 9 10 a ]',
                         self.sll1.__str__())

    def test_remove_start_of_list(self):
            self.assertEqual(10, len(self.sll1))
            for x in range(9, -1, -1):
                self.sll1.remove_start_of_list()
                self.assertEqual(x, len(self.sll1))
            self.assertEqual(0, len(self.sll1))
            self.assertEqual(10, len(self.sll2))
            self.assertEqual('[ 1 2 3 4 5 6 7 8 9 10 ]', self.sll2.__str__())
            self.sll2.remove_start_of_list()
            self.assertEqual('[ 2 3 4 5 6 7 8 9 10 ]', self.sll2.__str__())
            self.sll2.remove_start_of_list()
            self.assertEqual('[ 3 4 5 6 7 8 9 10 ]', self.sll2.__str__())

    def test_remove_following_node(self):
            self.assertEqual(3, len(self.sll4))
            self.assertEqual('[ begin mid end ]', self.sll4.__str__())
            self.sll4.remove_following_node(self.node3)
            self.assertEqual(2, len(self.sll4))
            self.assertEqual('[ begin mid ]', self.sll4.__str__())
            self.sll4.remove_following_node(self.node1)
            self.assertEqual(1, len(self.sll4))
            self.assertEqual('[ begin ]', self.sll4.__str__())
            self.sll4.remove_following_node(self.node1)
            self.assertEqual(0, len(self.sll4))

    def test_reverse_list_iterative(self):
        self.assertEqual(3, len(self.sll4))
        self.assertEqual('[ begin mid end ]', self.sll4.__str__())
        self.sll4.reverse_list_iterative()
        self.assertEqual('[ end mid begin ]', self.sll4.__str__())

    def test_recursive_algo(self):
        self.assertEqual(3, len(self.sll4))
        self.assertEqual('[ begin mid end ]', self.sll4.__str__())
        self.sll4.recursive_algo()
        self.assertEqual('[ end mid begin ]', self.sll4.__str__())

    def test_find_value(self):
        self.assertEqual('[ begin mid end ]', self.sll4.__str__())
        self.assertEqual('mid', self.sll4.find_value('mid').store)
        self.assertEqual('end', self.sll4.find_value('end').store)
        self.assertEqual('begin', self.sll4.find_value('begin').store)

if __name__ == "__main__":
    unittest.main()
