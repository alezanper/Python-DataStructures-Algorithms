def mingroups(arr, max):
    k = len(arr)
    i=1
    g=0
    while(k>0):
        k = len(arr)

        while(True):

            if (k==1):
                g += 1
                return g

            if(abs(arr[0]-arr[i])<=max):
                del(arr[i])
            else:
                i += 1

            if k == i:
                del(arr[0])
                break
        k = len(arr)
        g += 1
        i = 1
    return g

print(mingroups([3, 2, 1, 6, 7, 8, 9], 1))