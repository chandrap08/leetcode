def binarySearch(arr,n):

    half = int(len(arr)/2)
    print half,arr[half]

    if half > 0:
        if n == arr[half]:
            return arr.index(n)
        elif n < arr[half]:
            arr = arr[:half]
            #print arr
            binarySearch(arr,n)
        else:
            arr = arr[half:]
            #print arr
            binarySearch(arr,n)
    elif half == 0:
        if n == arr[half]:
            return n

b = binarySearch([2,3,4,5,6],2)
if b:
    print "Found"
else:
    print "Not found"
