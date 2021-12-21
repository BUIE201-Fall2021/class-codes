print(hash("test"))
print(hash("test"))

print(hash("test "))

print(hash(-100))

print(hash(0.423424))
print(hash(0.423425))

# collision
print(hash(0.1))
print(hash(230584300921369408))

class HashTable:
    def __init__(self) -> None:
        self._bucket_size = 100
        self._array = [None] * self._bucket_size
    
    def insert(self, value):
        hash_value = hash(value)
        index = hash_value % self._bucket_size
        if self._array[index] == None:
            self._array[index] = []
        self._array[index].append(value)

    def find(self, value):
        hash_value = hash(value)
        index = hash_value % self._bucket_size
        if self._array[index] == None:
            return False
        else:
            l = self._array[index]
            for v in l:
                if v == value:
                    return True
            return False
#            return value in l


h = HashTable()
h.insert("IE 201")
h.insert("IE 203")
h.insert("IE 515")

print(h.find("IE 201"))
print(h.find("IE 613"))
