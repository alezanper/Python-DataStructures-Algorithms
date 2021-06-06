some_list = [5, 4, 7, 1, -5, 9, 10, -3, 15, 8, 4]

def bubbleSort(to_sort_list):
    for i in range(len(to_sort_list)-1):
        for j in range(len(to_sort_list)-1):
            if to_sort_list[j] > to_sort_list[j+1]:
                temp = to_sort_list[j]
                to_sort_list[j] = to_sort_list[j+1]
                to_sort_list[j+1] = temp
    return to_sort_list

print(some_list)
print(bubbleSort(some_list))