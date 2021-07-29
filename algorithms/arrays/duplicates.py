# How do you find the duplicate number on a given integer array?

def duplicates(arr):
    dictionary = {}
    repeated = []

    for num in arr:
        if num not in dictionary:
            dictionary[num] = 1
        else:
            dictionary[num] += 1

    for key, value in dictionary.items():
        if value > 1:
            repeated.append([key, value])
    
    return repeated

arr = [1,2,3,14,11,3,24,2,6,32,2,6,38]

print(duplicates(arr))
