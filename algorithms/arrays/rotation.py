# A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become . Note that the lowest index item moves to the highest index in a rotation. This is called a circular array

def rotation(a, positions):

    k = len(a)
    new_array = a.copy()
    
    for i in range(k):
        new_index = i - positions
        
        if new_index < 0 :
            new_index = new_index + k 
        
        new_array[new_index] = a[i]
        
    return new_array

array = [1, 2, 3, 4, 5, 6, 7, 8]
positions = 1

print(array)
print(rotation(array, positions))