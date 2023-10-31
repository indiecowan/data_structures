import sys

class Node:
    def __init__(self, value, child : 'Node' = None):
        self.value = value
        self.child = child


class LinkedList:
    def __init__(self, head = None):
        self.head = Node(head)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        current = self.head
        while current.child != None:
            current = current.child
        current.child = Node(value)

    def insert(self, value, i):
        if self.head is None:
            print("ERROR in insert: i is out of bound for your linked list.")
            return -1
        current = self.head
        curr_i = 0
        while current.child != None and curr_i < i - 1:
            current = current.child
        if current.child is None:
            print("ERROR in insert: i is out of bound for your linked list.")
            return -1
        else:
            next = current.child
            current.child = Node(value)
            current.child.child = next
            return 0

    # index or -1 if not found
    def first_index(self, tofind) -> int:
        current = self.head
        i = 0
        while current != None and current != tofind:
            current = current.child
            i += 1
        return i if current != None else -1
    
    def print_list(self):
        sys.stdout.flush()
        print("in print list")
        current = self.head
        while current != None:
            print(current.value, " ")
            current = current.child
    


    