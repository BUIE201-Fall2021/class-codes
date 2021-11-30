# print
# size

class ListNode:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def print_node(self):
        print(self._value, end="")
        if self._next:
            self._next.print_node()
    
    def size_recursive(self):
        size = 1
        if self._next:
            size += self._next.size_recursive()
        return size

class LinkedList:
    def __init__(self):
        self._root = None
    
    def insert_first(self, value):
        new_node = ListNode(value)
        new_node._next = self._root
        self._root = new_node

    def print_list(self):
        print("[", end="")
        if self._root:
            self._root.print_node()
        print("]")
    
    # O(n)
    def size(self):
        if self._root:
            return self._root.size_recursive()
        else:
            return 0



m = LinkedList()
sz = m.size()


m.insert_first(3)
m.print_list()

m.insert_first(6)
m.print_list()

m.insert_first(1)
m.print_list()

sz = m.size()

i = 4