# [12-04-2018:3:45:23 IP Address 10.20.19.21 visited.]
def readLog(f):
    readTime = {}
    with open(f) as fread:
        line = fread.readlines()
        for l in line:
            w = l.split(" ")
            if w[3] not in readTime:
                readTime[w[3]] = []
                readTime[w[3]].append(w[0])
            else:
                readTime[w[3]].append(w[0])

    for k,v in readTime.items():
        if len(v) > 1:
            print(k,v[0],v[1])
        else:
            print(k,v[0])

filename = 'abc.log'
readLog(filename)
