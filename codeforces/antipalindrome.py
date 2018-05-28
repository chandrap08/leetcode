str = raw_input()

s_ord,count = ord(str[0]),1

for s in str[1:]:
    if ord(s) == s_ord:
        count += 1
if count == len(str):
    print 0
else:
    if (len(str) % 2) == 0:
        part2 = str[-(len(str)/2):]
        part1 = str[:len(str)/2]
        if part1 == part2[::-1]:
            substr = str[:len(str) -1]
            print len(substr)
        else:
            print len(str)
    else:
        part2 = str[-(len(str)-1)/ 2:]
        part1 = str[:(len(str) - 1) / 2]
        if part1 == part2[::-1]:
            substr = str[:len(str) - 1]
            print len(substr)
        else:
            print len(str)

