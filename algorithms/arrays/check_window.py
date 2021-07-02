# Given an array arr[] and size of array is n and one another key x, and give you a segment size k. 
# The task is to find that the key x present in every segment of size k in arr[].
# arr is an array
# k is the windows size
# x is the target
# Example:
# arr = [ 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3]
# x = 3 
# k = 3 
# Output : Yes 
# There are 4 non-overlapping segments of size k in the array, [3, 5, 2], [4, 9, 3], [1, 7, 3] and [11, 12, 3]. 3 is present all segments.

def check(arr, k, x):
    parts = []
    part = []
    limit = 0
    c = 1
    
    for i in range(len(arr)):
        limit = c*k
        if(i < limit):
            part.append(arr[i])
            continue
        parts.append(part.copy())
        part.clear()
        part.append(arr[i])
        c += 1

        if c*k > len(arr): 
            limit = len(arr) -1
    
    parts.append(part.copy())

    for part in parts:
        if (x not in part):
            return False

    return True

#arr = [ 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3]
#k = 3
#x = 3

#arr = [ 21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25]
#k = 5
#x = 23

arr = [5, 8, 7, 12, 14, 3, 9]
k = 2
x = 8
print(check(arr, k, x))
