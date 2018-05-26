class InterLeave(object):
    def parseArray(self,arr):
        interLeftArray = []
        k = 0
        l = len(arr)
        while l > 0:
            for item in arr:
                print (len(item),k,l,arr)
                if len(item) > k and l == 1:
                    interLeftArray.append(item[k:])
                elif len(item) > k and l > 1:
                    interLeftArray.append(item[k:][0])
                elif len(item) <= k:
                    arr.remove(item)
                    l = l -1

            k = k+1
        return interLeftArray

if __name__ == "__main__":
    i = InterLeave()
    a = i.parseArray([[1,2,3],[4,5],[3,3],[0,-2,4],[5,8,9,10,11,12]])
    print(a)