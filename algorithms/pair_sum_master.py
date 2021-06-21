# Given an integer array, output all the unique pairs that sum up to a specific value k
# pair_sum([1,3,2,2], 4)  returns 2 (1,3) and (2,2)

def pair_sum(array, sum):

    seen = set()
    output = set()

    for num in array:
        target = sum - num
        if target not in seen:
            seen.add(num)
            print(seen)
        else:
            output.add(((min(num,target)), max(num,target)))
            #print(output)

    return len(output)

a = [1,3,2,2]
sum = 4
print(pair_sum(a,sum))