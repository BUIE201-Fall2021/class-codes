
def binary_search(l, value):
    if (len(l) == 0):
        return False

    left = 0
    right = len(l) - 1

    while True:
        if left == right:
            return l[left] == value
        elif left == right - 1:
            return l[left] == value or l[right] == value
        else:
            middle = (left + right) // 2
            if l[middle] == value:
                return True
            elif l[middle] < value:
                left = middle + 1
            else: 
                right = middle -1

l = [-1, 2, 3, 5, 10, 15]

found5 = binary_search(l, 5)
print(found5)

found0 = binary_search(l, 0)
print(found0)
