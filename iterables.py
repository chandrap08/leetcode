# yield returns a generator only
def mygenerator():
    g = [1,2,3,4]
    for i in g:
        yield i*i

gen = mygenerator()
print(gen)
for i in gen:
    print(i)

for i in gen:
    print(i)