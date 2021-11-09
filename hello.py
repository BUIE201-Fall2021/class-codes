class Rectangle:
    def __init__(self, width, height) -> None:
        self._Width = width
        self._Height = height

    def print(self):
        for i in range(self._Height):
            for j in range(self._Width):
                print("*", end="")
            print("")
    
    def overridden_function(self):
        print("This is Rectangle's overridden_function")

class Square:
    def __init__(self, length) -> None:
        self._Length = length

    def print(self):
        for i in range(self._Length):
            for j in range(self._Length):
                print("*", end="")
            print("")

class NewSquare(Rectangle):
    def __init__(self, length) -> None:
        super().__init__(length, length)

    def my_additional_function(self):
        print("This function belongs to NewSquare")

    # function override mechanism
    def overridden_function(self):
        super().overridden_function()
        print("This is NewSquare's overridden_function")

print("Rectangle:")
rect = Rectangle(5, 8)
rect.print()

print("Square:")
sqr = Square(4)
sqr.print()

print("NewSquare:")
nsqr = NewSquare(6)
nsqr.print()
nsqr.my_additional_function()
nsqr.overridden_function()

# my_additional_function does not exist at Rectangle
# rect.my_additional_function()
rect.overridden_function()

class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("Hav")

class Cat(Animal):
    def talk(self):
        print("Miyav")

class Bird(Animal):
    def talk(self):
        print("Cik")

my_dog = Dog()
my_cat = Cat()
my_bird = Bird()

# Polymorphism
my_pets = [my_dog, my_cat, my_bird]
for pet in my_pets:
    pet.talk()

