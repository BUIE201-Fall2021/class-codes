import sys
import gc

print (globals())

x = "Hello, world"

print(gc.is_tracked(x))

sys.getrefcount(x)

print("Reference count: {}".format(sys.getrefcount(x)))

y = x

print(gc.get_count())

print("Reference count: {}".format(sys.getrefcount(x)))

del y

print("Reference count: {}".format(sys.getrefcount(x)))

del x

print("Reference count: {}".format(sys.getrefcount(x)))

print(issubclass(bool, int))
print(issubclass(int, float))
print(issubclass(int, object))

print(issubclass(list, object))

print (type([]))
print (type({}))
print (type(True))

matrix = []
for i in range(5):
    matrix.append([])
    for j in range(6):
        matrix[i].append(j)

print(matrix[3][5])