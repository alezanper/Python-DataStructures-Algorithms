# Given an array of integers (positive and negatives) find the largest continuous sum
# large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) -> 29

def large_cont_sum(array):
    
    large_sum = 0
    start_index = 0 
    end_index = 0
    k = len(array)

    for i in range(len(array)):
        large_sum += array[i]

    for i in range(len(array)):
        if((large_sum - array[i]) >= large_sum):
            large_sum = large_sum - array[i]
            start_index = i + 1
        else:
            break

    for i in range(len(array)):
        if((large_sum - array[k-i-1]) >= large_sum):
            large_sum = large_sum - array[k-i-1]
            end_index = k-i-1
        else:
            break

    # return array[start_index: end_index]
    return large_sum

print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))    # 29
print(large_cont_sum([-2,-3,4,-1,-2,1,5,-3]))   # 7