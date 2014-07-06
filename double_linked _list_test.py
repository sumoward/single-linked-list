"""
Brian Ward
06/07/2014

edit tests for  Double linked list to make it a double linked list

"""
import unittest
from double_linked_lists import Double_Linked_List

class dllTestCase(unittest.TestCase):

    def setUp(self):
        self.dll = Double_Linked_List()
        self.dll1 = Double_Linked_List()
        for x in range(1, 11):
            self.dll1.insert_end_of_list(x)
        self.dll2 = Double_Linked_List()
        for x in range(1, 11):
            self.dll2.insert_end_of_list(x)
        self.dll3 = Double_Linked_List()
        for x in range(11, 21):
            self.dll3.insert_end_of_list(x)
        self.dll4 = Double_Linked_List()
        self.node1 = self.dll4.insert_start_of_list('begin')
        self.node2 = self.dll4.insert_end_of_list('end')
        self.node3 = self.dll4.insert_node('mid', self.node1)

    def tearDown(self):
        pass

    def test__str__(self):
        self.assertEqual('[ begin mid end ]', self.dll4.__str__())
        self.assertEqual('[ 1 2 3 4 5 6 7 8 9 10 ]', self.dll1.__str__())
        self.assertEqual('[ 11 12 13 14 15 16 17 18 19 20 ]',
                          self.dll3.__str__())

    def test_isEmpty(self):
        self.assertEqual(0, len(self.dll))

    def test__len__(self):
        self.assertEqual(0, len(self.dll))
        node1 = self.dll.insert_start_of_list('begin')
        self.assertEqual(1, len(self.dll))
        self.dll.insert_end_of_list('end')
        self.assertEqual(2, len(self.dll))
        self.dll.insert_node('mid', node1)
        self.assertEqual(3, len(self.dll))

    def test_insert_end_of_list(self):
        for x in range(1, 11):
            self.dll.insert_end_of_list(x)
            self.assertEqual(x, self.dll.tail.store)
        self.assertEqual(10, len(self.dll))

    def test_insert_start_of_list(self):
        for x in range(1, 11):
            self.dll.insert_start_of_list(x)
            self.assertEqual(x, self.dll.head.store)
        self.assertEqual(10, len(self.dll))

    def test_insert_node(self):
        self.assertEqual(10, len(self.dll1))
        self.dll1.insert_node('a', self.dll1.tail)
        self.assertEqual('[ 1 2 3 4 5 6 7 8 9 10 a ]', self.dll1.__str__())
        self.assertEqual(11, len(self.dll1))
        node1 = self.dll1.insert_node('b', self.dll1.head)
        self.assertEqual('b', node1.__str__())
        self.assertEqual('[ 1 b 2 3 4 5 6 7 8 9 10 a ]', self.dll1.__str__())
        self.assertEqual(12, len(self.dll1))
        node2 = self.dll1.insert_node('c', node1)
        self.assertEqual('c', node2.__str__())
        self.assertEqual(13, len(self.dll1))
        self.assertEqual('[ 1 b c 2 3 4 5 6 7 8 9 10 a ]',
                         self.dll1.__str__())

    def test_remove_start_of_list(self):
        self.assertEqual(10, len(self.dll1))
        for x in range(9, -1, -1):
            self.dll1.remove_start_of_list()
            self.assertEqual(x, len(self.dll1))
        self.assertEqual(0, len(self.dll1))
        self.assertEqual(10, len(self.dll2))
        self.assertEqual('[ 1 2 3 4 5 6 7 8 9 10 ]', self.dll2.__str__())
        self.dll2.remove_start_of_list()
        self.assertEqual('[ 2 3 4 5 6 7 8 9 10 ]', self.dll2.__str__())
        self.dll2.remove_start_of_list()
        self.assertEqual('[ 3 4 5 6 7 8 9 10 ]', self.dll2.__str__())

    def test_remove_following_node(self):
        self.assertEqual(3, len(self.dll4))
        self.assertEqual('[ begin mid end ]', self.dll4.__str__())
        self.dll4.remove_following_node(self.node3)
        self.assertEqual(2, len(self.dll4))
        self.assertEqual('[ begin mid ]', self.dll4.__str__())
        self.dll4.remove_following_node(self.node1)
        self.assertEqual(1, len(self.dll4))
        self.assertEqual('[ begin ]', self.dll4.__str__())
        self.dll4.remove_following_node(self.node1)
        self.assertEqual(0, len(self.dll4))


    def test_remove_previous_node(self):
        self.assertEqual(3, len(self.dll4))
        self.assertEqual('[ begin mid end ]', self.dll4.__str__())
        self.dll4.remove_previous_node(self.node3)
        self.assertEqual(2, len(self.dll4))
        self.assertEqual('[ mid end ]', self.dll4.__str__())
        self.dll4.remove_previous_node(self.node2)
        self.assertEqual(1, len(self.dll4))
        self.assertEqual('[ end ]', self.dll4.__str__())
        self.dll4.remove_previous_node(self.node1)
        self.assertEqual(0, len(self.dll4))

#     def test_reverse_list_iterative(self):
#         self.assertEqual(3, len(self.dll4))
#         self.assertEqual('[ begin mid end ]', self.dll4.__str__())
#         self.dll4.reverse_list_iterative()
#         self.assertEqual('[ end mid begin ]', self.dll4.__str__())
# 
#     def test_recursive_algo(self):
#         self.assertEqual(3, len(self.dll4))
#         self.assertEqual('[ begin mid end ]', self.dll4.__str__())
#         self.dll4.recursive_algo()
#         self.assertEqual('[ end mid begin ]', self.dll4.__str__())

    def test_find_value(self):
        self.assertEqual('[ begin mid end ]', self.dll4.__str__())
        self.assertEqual('mid', self.dll4.find_value('mid').store)
        self.assertEqual('end', self.dll4.find_value('end').store)
        self.assertEqual('begin', self.dll4.find_value('begin').store)

if __name__ == "__main__":
    unittest.main()
