def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *=  i
    return result

def factorial_recursive(n):
    # base condition
    if n <= 1:
        return 1
    # recursive step / recursion
    n1 = factorial_recursive(n-1)
    return n * n1

recursive4 = factorial_recursive(4)
print(recursive4)

fact4 = factorial(5)
print(fact4)

fact1 = factorial(1)
print(fact1)

fact0 = factorial(0)
print(fact0)
