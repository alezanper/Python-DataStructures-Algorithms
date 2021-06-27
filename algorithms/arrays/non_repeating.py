# Find the first non-repeating element in a given array of integers.
# Input : [-1 2 -1 3 2]
# Output : 3

def non_repeating(arr):

    seen = set()
    repeated = set()

    for value in arr:
        if value not in seen:
            seen.add(value)
        else:
            repeated.add(value)

    for value in arr:
        if value not in repeated:
            return value

    return 0

print(non_repeating([-1, 2, -1, 3, 2]))