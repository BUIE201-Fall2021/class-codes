import ctypes
class Array:
    def __init__(self):
        self._array = None
        self._length = 0
    
    def insert(self, value):
        self._array = (1 * ctypes.py_object)()
        self._length = 1
        self._array[0] = value

    def print(self):
        print("[", end="")
        for i in range(self._length):
            print(self._array[i], end="")
        print("]")

m = Array()
m.insert(4)
m.print()

m.insert(6)
m.print()

i = 4