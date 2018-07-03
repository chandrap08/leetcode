from collections import Counter, defaultdict

p = [[1,2],[3,4],[5,6],[1,2]]
points = [(x[0],x[1]) for x in p]
a = list(Counter(points))

print(a)
#print(list(a.elements()))

# for counting use int
b = ['yellow','white','blue','orange','green','white','blue','yellow']
d = defaultdict(int)

for i in b:
    d[i] += 1

print(list(d.items()))

# for collecting the values
d = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

for k,v in s:
    d[k].append(v)

print(d)

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4), ('blue', 6)]
d = defaultdict(set)
for k,v in s:
    d[k].add(v)

print(d)