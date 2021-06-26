# Given an integer array, output all the unique pairs that sum up to a specific value k
# pair_sum([1,3,2,2], 4)  returns 2 (1,3) and (2,2)

def pair_sum(arr, sum):
    
    couples = 0

    while(len(arr) > 0):
        for i in range(1, len(arr)):
            if (arr[0] + arr[i] == sum):
                couples += 1
        
        del(arr[0])

    return couples

a = [1,3,2,2]
sum = 4
print(pair_sum(a,sum))