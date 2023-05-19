# find missing number on ordered array 

def missing(arr):
    flag = 0

    for i in range(len(arr)):
        if i == len(arr):
            break
        consecutive = arr[i+1] - arr[i]
        if consecutive > 1:
            return arr[i+1]-1
        
    return 0

print(missing([1,2,3,4,5,7,8,9]))
        
