str1 = raw_input();
t = int(str1)
import re

for i in range(t):
    str2 = raw_input()

    if 'R' and 'C' in re.split('[0-9]+',str2):
        rc = re.split('[A-Z]+', str2)
        rows = rc[1]
        column = int(rc[2])
        i = int(column/26)
        if i > 0:
            new_format = chr(i+64) + chr(int(column % 26) + 64) + rows
        else:
            new_format = chr(column + 64) + rows


    elif len(re.split('[0-9]+',str2)) == 2:
        column = re.split('[0-9]+', str2)[0]
        row = re.split('[A-Z]+',str2)[1]
        new_format = 'R' + row
        csum = 1
        for c in range(len(column) - 1):
            csum += (ord(column[c]) - 64) * 26
        csum += ord(column[-1]) - 65
        new_format += 'C' + str(csum)
        print new_format





