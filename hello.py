# insert
# find
# size
# remove
# print

class ListNode:
    def __init__(self, value):
        self._value = value
        self._next = None
class LinkedList:
    def __init__(self):
        self._root = None
    
    # O(1)
    def insert(self, value):
        new_node = ListNode(value)
        new_node._next = self._root
        self._root = new_node
    
    def print(self):
        print("[", end="")

        current_node = self._root
        while current_node != None:
            print(str(current_node._value), end=",")
            current_node = current_node._next
        print("]")

m = LinkedList()

m.insert(3)
m.print()

m.insert(6)
m.print()

# find1 = m.find(6)
# print(find1)

# find2 = m.find(-6)
# print(find2)

# m.remove_index(0)
# m.print()

i = 4