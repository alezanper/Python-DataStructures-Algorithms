# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
# extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
# 
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(arr):
    sum = 0
    flag = 0
    for num in arr:
        if flag == 1:
            if num == 7:
                flag = 0
            continue
        if num == 6:
            flag = 1
            continue
        sum += num
    
    return sum

print(sum67([1, 2, 2, 6, 99, 99, 7]))