# Given an unsorted array of integers, find the length of the longest consecutive elements sequence?

def sequence(arr):
    sequence = 1
    big = 0
    sequence_arr = []
    big_sequence = []

    for i in range(len(arr)-1):
        sequence_arr.append(arr[i])
        if (arr[i+1]-arr[i] == 1):
            sequence += 1
        else:
            if sequence > big:
                big = sequence
                big_sequence = sequence_arr.copy()
            else:
                sequence_arr.clear()

    return big_sequence

arr = [7, 1, 4, 3, 9, 1, 2, 3, 4, 6, 4, 9, 2, 5, 2, 7]
print(sequence(arr))