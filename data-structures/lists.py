list = [2, 3, 6, 6, 7, 1, 0, 4, -1, 4]
print(list) # [2, 3, 6, 6, 7, 1, 0, 4, -1, 4]

list.sort()
print(list) # [-1, 0, 1, 2, 3, 4, 4, 6, 6, 7]

print(list.index(4))    # first index of 4, index=5

list[5]=20
print(list) # Set 20 at index 5 [-1, 0, 1, 2, 3, 20, 4, 6, 6, 7]

list.append(100)
print(list) # Added 100 at the end of the list

list.pop()
print(list) # Removed 100 at the end of the list

list.pop(2)
print(list) # Removed digit at index 2

list.insert(2,1)
print(list) # add digit 1 at index 2

del(list[0])
print(list) # delete digit at index 0   [0, 1, 2, 3, 20, 4, 6, 6, 7]

print(list[3:5])    # Returns a list starting a index 3 and ending at index 4 [3, 20]
print(list[:5])    # Returns a list since beggining to index 4  [0, 1, 2, 3, 20]
print(list[5:])    # Returns a list since index 5 to the end [4, 6, 6, 7]

list.reverse()
print(list)   # Returns the reverse list [7, 6, 6, 4, 20, 3, 2, 1, 0]