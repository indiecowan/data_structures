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
    


    