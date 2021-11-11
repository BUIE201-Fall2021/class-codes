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

# representation of an integer vector
int_list = [4, 5, 9]

print (type(int_list))
print (type(int_list[0]))

# matrix representation
row1 = [4, 5, 9]
row2 = [3, 6, 8]

matrix = [row1, row2]

print (type(matrix))
print (type(matrix[0]))
print (type(matrix[0][0]))

n_rows = 2
n_cols = 3

m = []
for i in range(n_rows):
    m.append([])
    for j in range(n_cols):
        m[i].append(j)

def print_matrix(matrix):
    for row in matrix:
        for column in row:
            print (column, end="")
        print ("")

print("Original matrix")
print_matrix(m)

def transpose(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    transposed = []
    for i in range(n_cols):
        transposed.append([])
        for j in range(n_rows):
            transposed[i].append(matrix[j][i])
    
    return transposed

t = transpose(m)
print("Transposed")
print_matrix(t)

pause = 4