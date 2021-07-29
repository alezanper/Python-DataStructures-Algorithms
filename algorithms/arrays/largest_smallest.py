# How do you find the largest and smallest number in an unsorted integer array

def largest_smallest(arr):
    smallest = arr[0]
    largest = arr[0]

    for num in arr:
        if (num > largest):
            largest = num
        if (num < smallest):
            smallest = num

    return [smallest, largest]

arr = [2,4,1,14,21,7,8,5,4,9,4,6,0]
print(largest_smallest(arr))