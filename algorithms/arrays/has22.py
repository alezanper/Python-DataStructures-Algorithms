# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
# 
# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(arr):
    flag = 0

    for num in arr:
        if num == 2:
            flag += 1
        else:
            flag = 0
        
        if flag == 2:
            return True

    return False

print(has22([1, 2, 1, 2]))