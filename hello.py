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

def fibonacci_recursive(n):
    # base condition
    if n <= 2:
        return 1
    # recursion
    return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)

def fibonacci_recursive_cached(n, cache):
    # base condition
    if n <= 2:
        return 1
    # check cache 
    if n in cache:
        return cache[n]
    # insert into cache 
    cache[n] = fibonacci_recursive_cached(n-2, cache) + fibonacci_recursive_cached(n-1, cache)
    return cache[n]

fib3 = fibonacci(3)
fibrecursive5 = fibonacci_recursive(5)
fibcached5 = fibonacci_recursive_cached(5, {})

for i in range(1, 40):
    start = time.time()
    fibonacci(i)
    end = time.time()
    print("Iterative calculation of " + str(i) + " took " + str(end - start))

    start = time.time()
    fibonacci_recursive(i)
    end = time.time()
    print("Recursive calculation of " + str(i) + " took " + str(end - start))

    start = time.time()
    fibonacci_recursive_cached(i, {})
    end = time.time()
    print("Recursive cached calculation of " + str(i) + " took " + str(end - start))

