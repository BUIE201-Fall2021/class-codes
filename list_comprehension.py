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