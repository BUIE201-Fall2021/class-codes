import ctypes
class Array:
    def __init__(self):
        self._array = None
        self._length = 0
    
    # O(n)
    def insert(self, value):
        # allocate new array -> O(1)
        new_array = ((self._length + 1) * ctypes.py_object)()

        # copy existing items -> O(n)
        for i in range(self._length):
            new_array[i] = self._array[i]

        # insert the new item at the end -> O(1)
        new_array[self._length] = value

        # bookkeeping -> O(1)
        self._length += 1
        self._array = new_array

    # similar to in operator
    # O(n)
    def find(self, value):
        for i in range(self._length):
            if self._array[i] == value:
                return True
        return False

    # O(1)
    def size(self):
        return self._length
    
    # O(n)
    def remove_index(self, index):
        # allocate new array -> O(1)
        new_array = ((self._length - 1) * ctypes.py_object)()

        # copy existing items before index -> O(n)
        for i in range(index):
            new_array[i] = self._array[i]

        # copy existing items after index -> O(n)
        for i in range(index, self._length - 1):
            new_array[i] = self._array[i+1]

        # bookkeeping -> O(1)
        self._length -= 1
        self._array = new_array

    # O(1)
    def get_index(self, index):
        return self._array[index]

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

find1 = m.find(6)
print(find1)

find2 = m.find(-6)
print(find2)

m.remove_index(0)
m.print()

i = 4