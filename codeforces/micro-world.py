str = raw_input()
input_1 = map(int,str.strip().split())

str = raw_input()
input_2 = map(int,str.strip().split())

k = input_1[1]
arr = sorted(input_2)
removed = []
l = len(arr)
i = 0
while i <= l-2:
        print(l)
    #for i in range(l-1,-1,-1):
        for j in range(i+1,l):
            if arr[j] - arr[i] <= k and arr[i] > arr[j]:
                #removed.append(arr[j])
                del arr[i]
        i += 1
        l = len(arr)

print(len(arr))