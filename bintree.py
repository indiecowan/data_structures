class Node:
    # sets value and parent values, creates rightc and leftc fields + initializes to None
    def __init__(self, value) -> None:
        self.value = value
        self.leftc = None
        self.rightc = None

    def add(self, value : int) -> None:
        if value <= self.value:
            if self.leftc:
                self.leftc.add(value)
            else:
                self.leftc = Node(value)
        else:
            if self.rightc:
                self.rightc.add(value)
            else:
                self.rightc = Node(value)
    def row_array(self, array = None, row = 0) -> None:
        if array is None:
            array = []
        
        # print(array)
        if (len(array) - 1) < row:
            array.append([self.value])
        else:
            array[row].append(self.value)

        if self.leftc:
            self.leftc.row_array(array, row + 1)
        else:
            if (len(array) - 1) < (row + 1):
                array.append([None])
            else:
                array[row + 1].append(None)

        if self.rightc:
            self.rightc.row_array(array, row + 1)
        else:
            if (len(array) - 1) < (row + 1):
                array.append([None])
            else:
                array[row + 1].append(None)
        return array
    
    def print_node(self, row = 0) -> None:
        print("(r" + str(row) + ": " + str(self.value) + ")", end=" ")
        if self.leftc:
            self.leftc.print_node(row + 1)
        if self.rightc:
            self.rightc.print_node(row + 1)

class BinTree:
    def __init__(self, head : int = None) -> None:
        if head is not None:
            self.head = Node(head)
        else:
            self.head = None
    
    def add(self, value : int) -> None:
        if self.head:
            self.head.add(value)
        else:
            self.head = Node(value)

    # def is_in()

    def print_tree(self) -> None:
        print("Printing Tree:")
        rows = self.head.row_array()
        for row in rows:
            print(row)
