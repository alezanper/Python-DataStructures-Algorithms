# Given an array of n elements that contains elements from 0 to n-1, with any of these numbers appearing 
# any number of times. Find these repeating numbers in O(n) and using only constant memory space.
# Input : n = 7 and array[] = {1, 2, 3, 6, 3, 6, 1}
# Output: 1, 3, 6

def find_duplicates(arr):
    seen = set()
    duplicates = []
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
        else:
            duplicates.append(arr[i])
    
    return duplicates

def main():
    print(find_duplicates([1,2,3,4,6,7,2,3]))

if __name__ == '__main__':
    main()
