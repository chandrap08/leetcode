def partition(arr,start,pivotPoint):
    arr = arr[start,pivotPoint]
    pivot = arr[pivotPoint]

    for k,v in enumerate(arr):
        if v >= pivot:
            high = k
            continue
        else:
            low = k
            temp = arr[low]
            arr[k] = arr[high]
            arr[high] = temp
    return low + 1

def quicksort(arr,low,high):
    p = partition(arr,low,high)
    quicksort(arr,low,p-1)
    quicksort(arr,p+1,high)

a= [10,20,40,30,50,70,60]
n = len(a)
sortedarr = quicksort(a,0,n-1)
print sortedarr
