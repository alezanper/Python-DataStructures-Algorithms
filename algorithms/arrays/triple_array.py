# Given three arrays sorted in non-decreasing order, print all common elements in these arrays.
# Input: 
# arr1[] = {1, 5, 10, 20, 40, 80} 
# arr2[] = {6, 7, 20, 80, 100} 
# arr3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
# Output: 20, 80

def triple_array(arr1, arr2, arr3):
    dictionary = {}
    common_elements = []

    for value in arr1:
        if value in dictionary:
            dictionary[value] += 1
        else:
            dictionary[value] = 1

    for value in arr2:
        if value in dictionary:
            dictionary[value] += 1
        else:
            dictionary[value] = 1

    for value in arr3:
        if value in dictionary:
            dictionary[value] += 1
        else:
            dictionary[value] = 1

    for key, value in dictionary.items():
        if (value == 3):
            common_elements.append(key)

    return common_elements

arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(triple_array(arr1, arr2, arr3))