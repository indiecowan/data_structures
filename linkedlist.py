''' Linked List implementation in Python 
    Indie Cowan 2023 '''

class _Node:
    '''to be used by LinkedList
        - fields: value, next
        - methods: __init__, __repr__ '''
    def __init__(self, value, next : '_Node' = None):
        self.value = value
        self.next = next
    
    def __repr__(self) -> str:
        return "_Node: " + str(self.value)
    

class LinkedList:
    '''singly linked list
        - fields: head, tail, len
        - methods: append, insert, remove, get_at, find_first_index, print_list '''
    def __init__(self, head = None):
        '''initialized linked list
            - initializes head, tail and len
            - handles head value or no head value '''
        if head is None:
            self.head = None
            self.tail = None
            self.len = 0
        else:
            self.head = _Node(head)
            self.tail = self.head
            self.len = 1

    def __len__(self):
        '''returns length of linked list '''
        return self.len
    
    def __repr__(self) -> str:
        '''returns debugging representation string '''
        return "LinkedList:\nhead: " + repr(self.head) + "tail: " + repr(self.tail) + "len: " + str(self.len)
    
    def __str__(self):
        '''returns string representation of list'''
        result = ""
        current = self.head
        result += "["
        while current is not None and current.next is not None:
            result += str(current.value) + ", "
            current = current.next
        result += current.value + "]"

        return result
    
    def __iter__(self):
        '''returns iterable for list (self)'''
        self._iter_node = self.head
        return self
    
    def __next__(self):
        '''returns next item in iterable (self)'''
        if self._iter_node is None:
            raise StopIteration
        value = self._iter_node.value
        self._iter_node = self._iter_node.next
        return value
    
    def __getitem__(self, index):
        '''returns item at index, takes negative indicies
            - does not support slicing yet '''
        if index < 0:
            index = self.len + index
        if index < 0 or index >= self.len:
            raise IndexError("index out of bounds for LinkedList")
        return self._get_node_at(index).value

    def __setitem__(self, index, value):
        '''sets value at index, takes negative indicies
            - does not support slicing yet '''
        if index < 0:
            index = self.len + index
        if index < 0 or index >= self.len:
            raise IndexError("index out of bounds for LinkedList")
        node = self._get_node_at(index)
        node.value = value

    def __contains__(self, tofind):
        '''returns True if value is found in LL False otherwise'''
        return self.find_first_index(tofind) != -1
    
    def _get_node_at(self, index) -> _Node:
        '''returns (reference to) Node in LL at index i or None if it's out of range
            - does not take negative indicies'''
        i = 0
        curr_node = self.head
        while curr_node is not None and i < index:
            curr_node = curr_node.next
            i += 1
        return curr_node
    
    def is_empty(self):
        return self.head is None

    def append(self, value):
        '''adds element to end of list '''
        if self.head is None:
            self.head = _Node(value)
            self.tail = self.head
        else:
            self.tail.next = _Node(value)
            self.tail = self.tail.next
        self.len += 1

    def insert(self, value, index):
        '''adds element into list at given index, pushing other elements to the side (no overwriting)
        - will insert at the end of list (past current len)'''
        # check for negative indexing
        if index < 0:
            index = self.len + index

        new_node = _Node(value)
        # inserting at front
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.len:
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            prev_node = self._get_node_at(index - 1)
            if prev_node is None:
                raise IndexError("insert: index i is out of range for linked list")
            new_node.next = prev_node.next
            prev_node.next = new_node
        self.len += 1

    def remove(self, index):
        '''removes element at index i from linked list '''
        # check for negative indexing
        if index < 0:
            index = self.len + index

        # check i is within bounds
        if index >= self.len:
            raise IndexError("remove: index i is out of range for linked list")
        # check if it is head node
        if index == 0:
            self.head = self.head.next
        else:
            to_delete_parent = self._get_node_at(index - 1)
            to_delete = to_delete_parent.next
            if to_delete.next is None:
                self.tail = to_delete_parent
            else:
                to_delete_parent.next = to_delete.next
        self.len -= 1

    def clear(self):
        '''empties the list'''
        self.head = None
        self.tail = None
        self.len = 0

    def pop(self):
        '''removes and returns last value'''
        if self.is_empty():
            return None
        elif self.len == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.len -= 1
            return value
        else:
            value = self.tail.value
            self.tail = self._get_node_at(self.len - 2)
            self.tail.next = None
            self.len -= 1
            return value

    def get_at(self, index):
        '''gets value at specified index '''
        # check for negative indexing
        if index < 0:
            index = self.len + index
        
        node = self._get_node_at(index)
        if node is None:
            return None
        else:
            return self._get_node_at(index).value

    def find_first_index(self, tofind) -> int:
        '''returns index of first occurance or -1 if not found'''
        current = self.head
        i = 0
        while current is not None and current.value != tofind:
            current = current.next
            i += 1
        return -1 if current is None else i
    


    