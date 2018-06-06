inputString = raw_input()
inputArray = inputString.split(" ")
l = len(inputArray)

duplicates = []

for i in range(l):
    for j in range(i+1,l):
        if inputArray[i] not in duplicates:
            if inputArray[i] == inputArray[j]:
                    duplicates.append(inputArray[i])

for d in duplicates:
    print(d)