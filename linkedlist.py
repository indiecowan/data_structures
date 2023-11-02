''' Linked List implementation in Python 
    Indie Cowan 2023 '''

class _Node:
    def __init__(self, value, next : '_Node' = None):
        self.value = value
        self.next = next
    
    def __repr__(self) -> str:
        return "_Node: " + str(self.value)


class LinkedList:
    def __init__(self, head = None):
        if head is None:
            self.head = None
            self.tail = None
            self.len = 0
        else:
            self.head = _Node(head)
            self.tail = self.head
            self.len = 1

    def __len__(self):
        return self.len
    
    def __repr__(self) -> str:
        return "LinkedList: " + repr(self.head)
    
    '''_get_node_at
        - returns (reference to) Node in LL at index i'''
    def _get_node_at(self, i) -> _Node:
        curr_i = 0
        curr_node = self.head
        while curr_node is not None and curr_i < i:
            curr_node = curr_node.next
        return curr_node

    def append(self, value):
        if self.head is None:
            self.head = _Node(value)
            self.tail = self.head
        else:
            self.tail.next = _Node(value)
            self.tail = self.tail.next

        self.len += 1

    def insert(self, value, i):
        if self.head is None:
            if i == 0:
                self.head = _Node(value)
                self.tail = self.head
                self.len += 1
            else:
                raise IndexError("i is out of bound for your linked list.")
        else:
            current = self.head
            curr_i = 0
            while current.next != None and curr_i < i - 1:
                current = current.next
            if current.next is None:
                if i == self.len:
                    self.append(value)
                else:
                    raise IndexError("i is out of bound for your linked list.")
            else:
                next = current.next
                current.next = _Node(value)
                current.next.next = next
                self.len += 1

    '''remove
        - removes element at index i from linked list '''
    def remove(self, i):
        '''cases:
        removing head / tail node and need to update these values
        when head + tail are same node and that node is being removed
        removing node in the middle'''
        # check i is within bounds
        if i >= self.len:
            raise IndexError("remove: index i is out of range for linked list")
        # check if it is head node
        if i == 0:
            self.head = self.head.next
        else:
            to_delete_parent = self._get_node_at(i - 1)
            to_delete = to_delete_parent.next
            if to_delete.next is None:
                self.tail = to_delete_parent
            else:
                to_delete_parent.next = to_delete.next
        self.len -= 1


    # index or -1 if not found
    def find_first_index(self, tofind) -> int:
        current = self.head
        i = 0
        while current is not None and current.value != tofind:
            current = current.next
            i += 1
        return i if current is not None else -1
    
    def print_list(self):
        print("in print list")
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
    


    