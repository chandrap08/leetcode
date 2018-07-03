str1 = raw_input();


n = int(str1.split(" ")[0])
m = int(str1.split(" ")[1])
a = int(str1.split(" ")[2])

i = 1
j = 1
while True:
    if a * i < n:
        i += 1
    else:
        break

while True:
    if a * j < m:
        j += 1
    else:
        break

tiles = i * j
print tiles