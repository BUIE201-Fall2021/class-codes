print("Hello, world!")

# This is a single line comment
# This is another line of the comment
name = input("Please enter name:")  #everyting after number sign is ignored
print ("Hello, " + name)

"""
    This is actually a multi-line string
    But it will be ignored unless we assign it 
    to a variable. Hence it can be used as a comment.
"""

# Variable types:
# bool
b = True
f = False

# numerical
i = 4   #int 
j = 3.41    #float -> double in C
# complex numbers

# string
# either single or double quotes can be used
s = "Hello"
s2 = 'world'
# cannot mix and match s3 = "Hello'

# list
l = [3, 4, 2, 9]
print(l)

# list can be heterogeneous 
l2 = [3, "test", 4.12]
print(l2)
l2[1] = 5
print(l2)

# tuple
# similar to a list, but cannot be modified
t = (3, 5)
# t[1] = "test"

# dictionary
d = {
    "IE 201" : "Z. Caner Taşkın",
    "IE 203" : "Necati Aras"
}