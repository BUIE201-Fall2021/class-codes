class Rectangle:
    def __init__(self, width, height) -> None:
        self._Width = width
        self._Height = height

    def print(self):
        for i in range(self._Height):
            for j in range(self._Width):
                print("*", end="")
            print("")

class Square:
    def __init__(self, length) -> None:
        self._Length = length

    def print(self):
        for i in range(self._Length):
            for j in range(self._Length):
                print("*", end="")
            print("")

rect = Rectangle(5, 8)
rect.print()

sqr = Square(4)
sqr.print()