# from bintree import BinTree 

# mybintree = BinTree()

# mybintree.add(3)
# mybintree.print_tree()
# mybintree.add(4)
# mybintree.print_tree()
# mybintree.add(2)
# mybintree.print_tree()
# mybintree.add(5)
# mybintree.print_tree()
# mybintree.add(1)
# mybintree.print_tree()
# mybintree.print_tree()
# mybintree.add(7)
# mybintree.print_tree()
# mybintree.add(4)
# mybintree.print_tree()
# mybintree.add(1)
# mybintree.print_tree()

from linkedlist import LinkedList

myLL = LinkedList()
while True:
    newvalue = input("What do you want to add to your LL? ")
    myLL.append(newvalue)
    myLL.print_list()