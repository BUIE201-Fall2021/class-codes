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
