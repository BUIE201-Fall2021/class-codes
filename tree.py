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

class Tree:
    def __init__(self) -> None:
        self._root = None

    def insert(self, value):
        if self._root:
            self._root.insert_recursive(value)
        else:
            self._root = TreeNode(value)

m = Tree()
m.insert(20)
m.insert(10)
m.insert(30)
m.insert(5)
m.insert(15)
m.insert(25)
m.insert(40)

