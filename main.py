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
myLL.append(5)
# breakpoint()
myLL.print_list()
myLL.insert(15, 0)
myLL.print_list()
# breakpoint()
myLL.insert(12, 2)
myLL.print_list()
myLL.append(3)
myLL.print_list()
myLL.remove(1)
myLL.print_list()
print(myLL.find_first_index(15))
print(myLL.get_at(0))

while True:
    newvalue = input("What do you want to add to your LL? ")
    myLL.append(newvalue)
    myLL.print_list()