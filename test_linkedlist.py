import unittest
from linkedlist import LinkedList
class TestLinkedList(unittest.TestCase):
    '''tests for LinkedList'''
    # "happy path" (the expected use case), edge cases, and potential wrong inputs
    # __init__, __len__, __repr__, __str__, __iter__, __next__, __getitem__, __setitem__, __contains__, _get_node_at, is_empty, append, insert, remove, clear, pop, get_at (alias for __getitem__), set_at (alias for __setitem__), find_first_index
    
    def setUp(self):
        '''called before every test'''
        self.list = LinkedList()

    def populate_list(self, len = 10) -> None:
        '''for when a function works on a full array'''
        for i in range(len):
            self.list.append(i)

    def test__init__(self):
        # list was __init__ wout value
        self.assertFalse(self.list is None)
        self.assertEqual(self.list.len, 0)
        self.assertTrue(self.list.head is None)
        self.assertTrue(self.list.tail is None)

        # init w value
        self.list = LinkedList(3)
        self.assertFalse(self.list is None)
        self.assertEqual(self.list.len, 1)
        self.assertEqual(self.list.head.value, 3)
        self.assertEqual(self.list.tail.value, 3)
        self.assertEqual(self.list.head, self.list.tail)

    def test__len__(self):
        '''depends on __init__, self.populate_list and clear, tests insert, append, remove, pop len handling
            - this isn't really a test on the function bc it returns a field but a test on the handling of the field'''
        # check we start w an empty list
        self.assertEqual(self.list.len, 0)

        # test insert's len handling
        # empty list
        self.list.insert(1, 0)
        self.assertEqual(len(self.list), 1)
        # front of list
        self.list.insert(0, 0)
        self.assertEqual(len(self.list), 2)
        # back of list
        self.list.insert(2, 2)
        self.assertEqual(len(self.list), 3)
        # middle of list
        self.list.insert(1.5, 2)
        self.assertEqual(len(self.list), 4)

        # test clear's len handling
        self.list.clear()
        self.assertEqual(self.list.len, 0)

        # test append's len handling
        # list starts empty
        # empty list
        self.list.append(1)
        self.assertEqual(len(self.list), 1)
        # other times (appending to end)
        self.list.append(2)
        self.assertEqual(len(self.list), 2)

        # test remove's len handling
        self.list.append(3)
        self.list.append(4)
        # list starts as 1, 2, 3, 4
        og_len = len(self.list)
        # middle of list
        self.list.remove(1)
        self.assertEqual(self.list.len, og_len - 1)
        # front of list
        self.list.remove(0)
        self.assertEqual(self.list.len, og_len - 1)
        # end of list
        self.list.remove(1)
        self.assertEqual(self.list.len, og_len - 1)
        # last element in list
        self.list.remove(0)
        self.assertEqual(self.list.len, og_len - 1)

        # test pop's len handling
        self.populate_list(2)
        # start w list 1, 2
        # not last element in list
        self.list.pop()
        self.assertEqual(len(self.list), 1)
        # last element in list
        self.list.pop()
        self.assertEqual(len(self.list), 0)




    def test_append(self):
        '''depends on __init__ and __getitem__'''
        # Test the append method
        self.list.append(1)
        self.assertEqual(len(self.list), 1) # Check that length is updated
        self.assertEqual(self.list[0], 1)   # Check that the added item is retrievable
        self.append(2)
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list[0], 2)

    def test_


    
