# Find the largest three distinct elements in an array
# Input: arr[] = {10, 4, 3, 50, 23, 90}
# Output: 90, 50, 23

def largest_three (arr):

    largest = [0]*3

    for i in range(len(arr)):
        if arr[i] > largest[0]:
            largest[0] = arr[i]

    for i in range(len(arr)):
        if arr[i] > largest[1] and arr[i] not in largest:
            largest[1] = arr[i]

    for i in range(len(arr)):
        if arr[i] > largest[2] and arr[i] not in largest:
            largest[2] = arr[i]

    return largest

print(largest_three([10, 4, 3, 50, 23, 90]))

