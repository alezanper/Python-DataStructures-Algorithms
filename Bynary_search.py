import math

def binarySearch(sortList, x):
    start = 0
    end = len(sortList)-1
    while(start <= end):
        middle = math.floor((start + end)/2)
        if (sortList[middle] < x):
            start = middle + 1
        elif (sortList[middle] > x):
            end = middle - 1
        else :
            return middle
    return -1

sortList = [-12,-5,-2,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,20]

print(binarySearch(sortList, -12))
print(binarySearch(sortList, 73))
print(binarySearch(sortList, 20))
print(binarySearch(sortList, -98))