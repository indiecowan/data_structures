''' Double ended queue implementation using linked list 
    Indie Cowan 2023 '''
from linkedlist import LinkedList

class DEQ:
    def __init__(self):
        self.queue = LinkedList()

    def push(self, value):
        self.queue.insert(0)
