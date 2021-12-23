# O(n^2)
def bubble_sort(l):
    print(l)
    while True:
        already_sorted = True
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                already_sorted = False
                l[i], l[i+1] = l[i + 1], l[i]
                print(l)
        if already_sorted:
            return

l = [3, 10, 5, 2, -1, 15]
bubble_sort(l)

inverse_sorted = [15, 10, 5, 3, 2, -1]
bubble_sort(inverse_sorted)

# best sorting algorithms work in O(n log(n)) time
# quicksort, mergesort, heapsort
# timsort