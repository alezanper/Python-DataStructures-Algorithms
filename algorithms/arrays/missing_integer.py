# You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

def missing_integer(arr):
    for i in range(len(arr)):
        if (i < len(arr)-1):
            if (arr[i+1]-arr[i]>1):
                return arr[i] +1
    return 0

print(missing_integer([1,2,3,4,5,6,8,9]))