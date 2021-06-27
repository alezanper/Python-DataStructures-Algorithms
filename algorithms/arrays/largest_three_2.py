# Find the largest three distinct elements in an array
# Input: arr[] = {10, 4, 3, 50, 23, 90}
# Output: 90, 50, 23

def largest_three (arr):

    first, second, third = -1

    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            third = second
            first = arr[i]
        elif arr[i] > second:
            third = second
            second = arr[i]
        elif arr[i] > third:
            third = arr[i]
    return [first, second, third]

print(largest_three([10, 4, 3, 50, 23, 90]))

