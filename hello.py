import time

def fibonacci(n):
    if n <= 2:
        return 1
    prev = 1
    prev2 = 1
    for i in range(n-2):
        current = prev + prev2
        prev2 = prev
        prev = current
    return current


start = time.time()
fib3 = fibonacci(3)
end = time.time()
print (end - start)

# for i in range(1, 1010):
#     start = time.time()
#     factorial(i)
#     end = time.time()
#     print("Iterative calculation of " + str(i) + " took " + str(end - start))

#     start = time.time()
#     factorial_recursive(i)
#     end = time.time()
#     print("Recursive calculation of " + str(i) + " took " + str(end - start))

