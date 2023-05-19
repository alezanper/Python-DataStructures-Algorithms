from abc import abstractproperty


# Consider an array non-negative integers. A second array is formed by shuffling the elements of the first array and 
# deleting a random element. Given these two arrays. Find which element is missing in the second abstractproperty
# finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])    # Returns 5

def missing_element(a, b):

    if (len(a)<1 or len(b)<1):
        return 0
    total_a = 0
    total_b = 0

    for i in range(len(a)):
        total_a += a[i]
    
    for i in range(len(b)):
        total_b += b[i]
    
    return total_a - total_b

a = [1, 2, 3, 4, 5, 6, 7]
b = [3, 7, 2, 1, 4, 6]

print(missing_element(a, b))