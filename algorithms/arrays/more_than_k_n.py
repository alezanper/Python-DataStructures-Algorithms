# Given an array of size n, find all elements in array that appear more than n/k times. For example, if 
# the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. Note that 
# size of array is 8 (or n = 8), so we need to find all elements that appear more than 2 (or 8/4) times. 
#  are two elements that appear more than two times, 2 and 3. 

def rep(arr, k):
    repeated = []
    dictionary = {}
    
    for i in range(len(arr)):
        if arr[i] not in dictionary:
            dictionary[arr[i]] = 1
        else:
            dictionary[arr[i]] += 1

    for key, value in dictionary.items():
        if (value > (len(arr)/k)):
            repeated.append(key)
    
    return repeated

print(rep([3, 1, 2, 2, 1, 2, 3, 3], 4))
