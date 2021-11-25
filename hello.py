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
    def insert_first(self, value):
        new_node = ListNode(value)
        new_node._next = self._root
        self._root = new_node
    
    # O(n)
    def insert_last(self, value):
        new_node = ListNode(value)
        if self._root == None:  # empty list
            self._root = new_node
        else:   # full list
            current_node = self._root
            while current_node != None:
                if current_node._next == None:
                    break
                else:
                    current_node = current_node._next
            current_node._next = new_node
    
    # O(n)
    def find(self, value):
        current_node = self._root
        while current_node != None:
            if current_node._value == value:
                return True
            else:
                current_node = current_node._next
        return False
    
    # O(n)
    def size(self):
        count = 0
        current_node = self._root
        while current_node != None:
            count += 1
            current_node = current_node._next
        return count

    # O(1)
    def remove_first(self):
        if self._root != None:
            self._root = self._root._next
    
    # O(n)
    def remove_last(self):
        if self._root == None:  # list is empty
            return
        elif self._root._next == None: # list has exactly one element
            self._root = None
        else:   # list has at least two elements
            prev_node = None
            current_node = self._root
            while current_node != None and current_node._next != None:
                prev_node = current_node
                current_node = current_node._next
            prev_node._next = None

    def print(self):
        print("[", end="")

        current_node = self._root
        while current_node != None:
            print(str(current_node._value), end=",")
            current_node = current_node._next
        print("]")

m = LinkedList()

m.insert_first(3)
m.print()

m.insert_first(6)
m.print()

m.insert_last(5)
m.print()

find1 = m.find(6)
print(find1)

find2 = m.find(-6)
print(find2)

count = m.size()

m.remove_last()
m.print()

m.remove_last()
m.print()

i = 4