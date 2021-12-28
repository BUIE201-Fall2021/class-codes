list_lowercase = ["tomato", "potato", "cabbage", "lettuce"]
print(list_lowercase)

# explicit list creation loop
list_uppercase = []
for x in list_lowercase:
    list_uppercase.append(x.upper())

print(list_uppercase)

# equivalent list comprehension
list_comp_uppercase = [x.upper() for x in list_lowercase]

print(list_comp_uppercase)


# create a list that consists of squares of the first 10 integers

list_squares_explicit = []
for i in range(10):
    list_squares_explicit.append(i * i)

list_squares = [i * i for i in range(10)]
print(list_squares)

# create a list that consists of squares of the first 5 odd integers
list_squares_odd_explicit = []
for i in range(10):
    if i % 2:
        list_squares_odd_explicit.append(i * i)
print (list_squares_odd_explicit)

# equivalent to
list_squares_odd = [i * i for i in range(10) if i % 2]
print (list_squares_odd)
