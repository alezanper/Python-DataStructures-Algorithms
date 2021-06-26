def mingroupsroups(arr, max):
    k = len(arr)
    i = 1
    groups=0
    while(k>0):

        while(True):
            k = len(arr)

            if (k==1):
                groups += 1
                return groups

            if(abs(arr[0]-arr[i])<=max):
                del(arr[i])
            else:
                i += 1

            if k == i:
                del(arr[0])
                break
        groups += 1
        i = 1
    return groups

print(mingroupsroups([3, 2, 1, 6, 7, 8, 9], 1))