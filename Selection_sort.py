def selectionSort(some_list): 
    for i in range(len(some_list)):
        for j in range(i+1, len(some_list)):
            if some_list[j] < some_list[i]:
                temp = some_list[i]
                some_list[i] = some_list[j]
                some_list[j] = temp
    return some_list


u_list = [5, 4, 7, 1, -5, 9, 10, -3, 15, 8, 4]
print(selectionSort(u_list))