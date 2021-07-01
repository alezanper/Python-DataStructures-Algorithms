# Given an array that contains both positive and negative integers, find the product of the maximum 
# product subarray. Expected Time complexity is O(n) and only O(1) extra space can be used.
# Input: arr[] = {6, -3, -10, 0, 2}
# Output:   180  // The subarray is {6, -3, -10}

def prods(arr):
    product = current_product = arr[0] * arr[1] 

    for num in arr[2:]:
        current_product = max(current_product * num, num)
        product = max(current_product, product)
    return product


print(prods([8,1,2,-3,4,5,-1])) # 20