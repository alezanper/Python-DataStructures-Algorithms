# How do you find the missing number in a given integer array of 1 to 30?

def missing30(arr):
    for i in range(len(arr)-1):
        if(arr[i+1]-arr[i]>1):
            return arr[i+1]-1
    return -1

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
print(missing30(arr))   # 14