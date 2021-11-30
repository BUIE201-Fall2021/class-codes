# print
# size
# find
class ListNode:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def print_node(self):
        print(self._value, end="")
        if self._next:
            self._next.print_node()

    def print_node_reverse(self):
        if self._next:
            self._next.print_node_reverse()
        print(self._value, end="")

    # O(n)
    def size_recursive(self):
        size = 1
        if self._next:
            size += self._next.size_recursive()
        return size
    
    # O(n)
    def find_recursive(self, value):
        if self._value == value:
            return True
        elif self._next:
            return self._next.find_recursive(value)
        else:
            return False
class LinkedList:
    def __init__(self):
        self._root = None
    
    def insert_first(self, value):
        new_node = ListNode(value)
        new_node._next = self._root
        self._root = new_node

    # O(n)
    def print_list(self):
        print("[", end="")
        if self._root:
            self._root.print_node()
        print("]")

    def print_list_reverse(self):
        print("[", end="")
        if self._root:
            self._root.print_node_reverse()
        print("]")

    # O(n)
    def size(self):
        if self._root:
            return self._root.size_recursive()
        else:
            return 0
    
    # O(n)
    def find(self, value):
        if self._root:
            return self._root.find_recursive(value)
        else:
            return False




m = LinkedList()
sz = m.size()


m.insert_first(3)
m.print_list()

m.insert_first(6)
m.print_list()

m.insert_first(1)
m.print_list()
m.print_list_reverse()

sz = m.size()

find1 = m.find(6)
print(find1)

find2 = m.find(-6)
print(find2)

i = 4