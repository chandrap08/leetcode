n = int(raw_input())
strList = []
for _ in range(1,n+1):
    input_str = raw_input()
    strList.append(input_str)

lenList = [[len(s),s] for s in strList]

def findString(lenList):
    finalList = []
    for k in range(len(lenList)-1):
            if lenList[k][1] in lenList[k+1][1]:
                finalList.append(lenList[k][1])
                continue
            else:
                return False
    finalList.append(lenList[-1][1])
    return finalList

listSorted = sorted(lenList)
finalList = findString(listSorted)
if finalList:
    print("YES")
    for k,v in enumerate(finalList):
        print(v)
else:
    print("NO")




