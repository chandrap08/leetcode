def examples(d):
    for i in d:
        if i % 2 == 0:
            d.remove(i)
            d.append(i*2)
    print(d)

e = examples([1,2,3,4,5,6,7,8])


import itertools

a,b,c = [1,2,3],[4,5,6],[7,8,9]
#print(list(itertools.permutations(a)))
# print(list(itertools.chain(a,b,c)))
# print(list(itertools.chain(a,b)))
# print(list(itertools.combinations(list(itertools.chain(a,b)),2)))

#d = list(itertools.chain(a,b,c))




