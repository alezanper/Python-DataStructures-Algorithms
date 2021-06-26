# Given two sorted arrays, find their union and intersection.
# Input : arr1[] = {1, 3, 4, 5, 7}
#         arr2[] = {2, 3, 5, 6} 
# Output : Union : {1, 2, 3, 4, 5, 6, 7} 
#          Intersection : {3, 5}

def union_interception(arr1, arr2):
    union = arr1 + arr2
    union = set(union)
    interception = []

    for i in range(len(arr1)):
        if arr1[i] in arr2:
            interception.append(arr1[i])
    
    return(union, interception)


print(union_interception([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8]))