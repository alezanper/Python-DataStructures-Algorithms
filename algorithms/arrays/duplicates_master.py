# How do you find the duplicate number on a given integer array?

def duplicates(arr):
    seen = set()
    repeated = set()

    for num in arr:
        if num not in seen:
            seen.add(num)
        else:
            repeated.add(num)
    
    return repeated

arr = [1,2,3,14,11,3,24,2,6,32,2,6,38]

print(duplicates(arr))
