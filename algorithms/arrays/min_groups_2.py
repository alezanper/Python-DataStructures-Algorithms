def mingroupsroups(arr, max):

    arr.sort()

    k = len(arr)
    groups = 0
    while(k > 0):

        while(True):
            k = len(arr)

            if (k==1):
                groups += 1
                return groups

            if(abs(arr[0]-arr[1])<=max):
                del(arr[1])
            else:
                del(arr[0])
                break
            
        groups += 1
    return groups

print(mingroupsroups([3, 2, 1, 6, 7, 8, 9], 3))