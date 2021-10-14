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
