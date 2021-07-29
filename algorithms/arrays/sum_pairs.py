# How do you find all pairs of an integer array whose sum is equal to a given number?

def pair_sum(arr, sum):
    seen = set()
    target = 0
    couples = []

    for num in arr:
        target = sum - num
        if target not in seen:
            seen.add(num)
        else: 
            couples.append([num, sum-num])

    return couples

arr = [1,2,3,4,5,6,7,8,9]
sum = 5

print(pair_sum(arr, sum))