# given an array [2,3,4,5,6,1,4,1,4,1] find the couples that can sum 7

def sum(arr, sum):
	couples = []
	seen = set()
	
	target = 0
	i = 1
	
	for i in range(len(arr)):
		target = sum - arr[i]
		
		if target not in seen:
			seen.add(arr[i])
		else:
			couples.append([arr[i], sum - arr[i]])

	return couples

print(sum([8,2,3,4,5,6,1], 7))