# Given an array of integers (positive and negatives) find the largest continuous sum
# large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) -> 29

def large_cont_sum(array):

    max_sum = current_sum = array[0]
    
    for num in array[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum


print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))    # 29
print(large_cont_sum([-2,-3,4,-1,-2,1,5,-3]))   # 7