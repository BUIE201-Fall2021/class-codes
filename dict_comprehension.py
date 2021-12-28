list_lowercase = ["tomato", "potato", "cabbage", "lettuce"]
print(list_lowercase)

# explicit dictionary creation
dict_uppercase = {}
for x in list_lowercase:
    dict_uppercase[x] = x.upper()

print(dict_uppercase)

# dictionary comprehension
dict_uppercase_comprehension = {x:x.upper() for x in list_lowercase}

print(dict_uppercase_comprehension)