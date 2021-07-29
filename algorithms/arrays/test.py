# Given an integer array, output all the unique pairs that sum up to a specific value k
# pair_sum([1,3,2,2], 4)  returns 2 (1,3) and (2,2)

def sum (arr, sum):

	target = 0
	seen = set()
	couples = []

	for num in arr:
		target = sum - num
		if target not in seen:
			seen.add(num)
		else:
			couples.append([num, sum-num])
	
	return couples

print(sum([3,5,0,4,2,2,1], 4))