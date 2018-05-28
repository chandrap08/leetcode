str = raw_input()
l = {}
for _ in range(int(str)):
    str = raw_input()
    x,y = map(int,str.split(" "))
    if x in l:
        l[x] = max(l[x],y)
    else:
        l[x] = y

str = raw_input()
for _ in range(int(str)):
    str = raw_input()
    x, y = map(int, str.split(" "))
    if x in l:
        l[x] = max(l[x],y)
    else:
        l[x] = y

profit = 0

for k,v in l.iteritems():
    profit += v

print(profit)

