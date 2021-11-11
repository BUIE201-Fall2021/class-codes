import sys

b = True
print(type(b))

i = 42
print(type(i))

# bool is an int in Python

print(issubclass(bool, int)) 
print(issubclass(int, bool))

p = 3.41
print(type(p))

# int is not a special kind of float in Python
print(issubclass(int, float)) 

# example of inexact floating point arithmetic in Python
# https://docs.python.org/3/tutorial/floatingpoint.html
print (0.1 + 0.1 + 0.1 == 0.3)

print(issubclass(int, object))
print(issubclass(float, object))
print(issubclass(str, object))

l = [4, 7.8, "string"]
print(l)
print(type(l))
for i in l:
    print(type(i))

print(type(print))

def foo():
    print ("Hello from foo")

print(type(foo))
class MyClass:
    def __init__(self) -> None:
        pass

c = MyClass()
print(type(c))
print(type(MyClass))

int_list = [4, 5, 9]

print (type(int_list))
print (type(int_list[0]))

