def insertionSort(some_list):
    for i in range(1, len(some_list)):
        search_index = i
        insert_value = some_list[i]
        while search_index > 0 and some_list[search_index-1] > insert_value :
            some_list[search_index] = some_list[search_index-1]
            search_index -= 1
            some_list[search_index] = insert_value
            
    return some_list

u_list = [5, 4, 7, 1, -5, 9, 10, -3, 15, 8, 4]
print(insertionSort(u_list))