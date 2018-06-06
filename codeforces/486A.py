i = map(int,(raw_input().split()))
#print i
rates_list = map(int,raw_input().split())
rates = {v:k for k,v in enumerate(rates_list)}

if len(rates.keys()) >= i[1]:
    team = []
    s = ""
    count = 0
    for r in sorted(rates.keys()):
        if count < i[1]:
            s = s + " " + str(rates[r] + 1)
            count += 1
    print "YES"
    print s.strip()


else:
    print "NO"
