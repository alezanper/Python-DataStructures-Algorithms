# Given an array of integers, find the first repeating element in it. We need to find the element that 
# occurs more than once and whose index of first occurrence is smallest. 
# Input:  arr[] = {10, 5, 3, 4, 3, 5, 6}
# Output: 5 [5 is the first element that repeats]

def first_repeting(arr):

    seen = set()
    repeted = set()

    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
        else:
            repeted.add(arr[i])
    
    for i in range(len(arr)):
        if arr[i] in repeted:
            return arr[i]

    return 0
    
print(first_repeting([10, 5, 3, 4, 3, 5, 6]))
