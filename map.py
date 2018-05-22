def square(x):
    return x*x

def add(n):
    return n + 2

a = [1,2,3,4,5]
funcs = [square,add]
for i in range(5):
    b = list(map(lambda a:a(i),funcs))
    print b


c = list(map(lambda x: add(x),a))
print c

num_list = range(-5,5)
d = list(filter(lambda x: x < 0, num_list))
print d

print num_list
from functools import *
e = reduce(lambda x,y: x*y,num_list)
print e
