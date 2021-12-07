class TreeNode:
    def __init__(self, value) -> None:
        self._value = value
        self._left = None
        self._right = None
    
    def insert_recursive(self, value):
        if value <= self._value:
            if self._left:
                self._left.insert_recursive(value)
            else:
                self._left = TreeNode(value)
        else:
            if self._right:
                self._right.insert_recursive(value)
            else:
                self._right = TreeNode(value)
    
    def size_recursive(self):
        size_left = 0
        if self._left:
            size_left = self._left.size_recursive()

        size_right = 0
        if self._right:
            size_right = self._right.size_recursive()
        
        return 1 + size_right + size_left

class Tree:
    def __init__(self) -> None:
        self._root = None

    # O(log n)
    def insert(self, value):
        if self._root:
            self._root.insert_recursive(value)
        else:
            self._root = TreeNode(value)
    
    # O(n)
    def size(self):
        if self._root:
            return self._root.size_recursive()
        else:
            return 0

m = Tree()
print (m.size())

m.insert(20)
m.insert(10)
m.insert(30)

print (m.size())

m.insert(5)
m.insert(15)
m.insert(25)
m.insert(40)

print (m.size())
