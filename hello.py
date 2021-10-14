def greet(name = "Stranger"):
    # statements
    i = 10  # local variable
    print("Hello " + name + " I am function")
    print ("i = " + str(i))

my_global = "caner"  # global variable -> don't use global variables!
greet(my_global)

# cannot access local variable outside of the function
# i += 40 


def calculate_area (width, height):
    return width * height

area = calculate_area(4, 6)
print(area)

greet() # using default parameters

# optional parameters have to be defined after required parameters
def my_function(a, b = 0):
    print (str(a) + " " + str(b))

# positional arguments
my_function(1, 5)
my_function(1)

# keyword arguments
my_function (a = 5, b = 10)
my_function (b = 10, a = 5)

# arbitrary positional arguments as tuple
def sum_all(*values):
    total = 0
    for value in values:
        total += value
    return total

sum = sum_all(4, 5, 5, 6, 2, 6)
print(sum)

sum = sum_all()
print(sum)

sum = sum_all(4, 5)
print(sum)

# arbitrary keyword arguments as dict
# kwargs

# In C/C++ function overloading is possible
# multiple functions with the same name but different parameters
# function overloading is not supported in Python.