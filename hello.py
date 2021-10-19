def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *=  i
    return result

fact4 = factorial(5)
print(fact4)

fact1 = factorial(1)
print(fact1)

fact0 = factorial(0)
print(fact0)
