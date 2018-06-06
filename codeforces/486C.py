from functools import reduce

n = int(raw_input())
s = []
for i in range(n):
    k = int(raw_input())
    l = map(int,str(raw_input()).split())
    suml = reduce((lambda a, b: a + b), l)
    s.append([l,suml])


def equalSums(s):
    for k,v in enumerate(s):
        for j in s[k+1:]:
           diff = v[1] - j[1]
           for num in set(v[0]):
               for l in set(j[0]):
                    diffInDigit = abs(num - l)
                    if diff == diffInDigit:
                        res = [k,v[0].index(num),s[k+1:].index(j) + k + 1,j[0].index(l)]
                        return res
                    else:
                        continue
    return False

e = equalSums(s)
if e:
    print "YES"
    print("%d %d"% (e[0] + 1, e[1] + 1))
    print("%d %d"% (e[2] + 1, e[3] + 1))
else:
    print "NO"
