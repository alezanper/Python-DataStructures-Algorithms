# Given an integer array, output all the unique pairs that sum up to a specific value k
# pair_sum([1,3,2,2], 4)  returns 2 (1,3) and (2,2)

def pair_sum(array, sum):
    pairs = 0
    couplecreated = False

    k = len(array)

    if(k <= 1):
        return 0

    while(k>1):
        for i in range(1, k, 1):
            if(array[0] + array[i] == sum):
                couplecreated = True
                del(array[0])
                del(array[i-1])
                break
        if(couplecreated):
            pairs += 1
            k = len(array)
            couplecreated = False
        else:
            del(array[0])
    return pairs

a = [1,3,2,2]
sum = 4
print(pair_sum(a,sum))