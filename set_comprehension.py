list_duplicates = [1, 3, 0, 1, 0, -3, 10, 15]

print("Number of integers: " + str(len(list_duplicates)))

set_of_list = set(list_duplicates)

print("Number of distict integers: " + str(len(set_of_list)))
for i in set_of_list:
    print(i)

check_10_list = 10 in list_duplicates   #linear search O(n)
check_10_set = 10 in set_of_list    # hash search O(1)


# create a set that consists of squares of the first 5 odd integers
set_squares_odd_explicit = set()
for i in range(10):
    if i % 2:
        set_squares_odd_explicit.add(i * i)
print (set_squares_odd_explicit)

# equivalent to
set_squares_odd = {i * i for i in range(10) if i % 2}
print (set_squares_odd)
